<template>
  <div class="container">
    <div class="profile">
      <template
        v-if="fileError">
        <p class="w-100 text-danger fs-6">
          {{ fileErrorMsg }}
        </p>
      </template>
      <div class="upload-img">
        <div 
        class="upload-img__avatar border"
        :class="{'border-danger': userImgIsNull}">
        <template 
        v-if="imgToUpload">
        {{ imgToUpload }}
        </template>
        <template v-else>
          <img src="../../assets/images/avatar.jpg" alt="Avatar">
        </template>
        </div>
        <div class="upload-img__file">
          <label for="new-img">
            <span 
            class="d-flex align-items-center justify-content-center">
              <span class="pr-1 pl-1 py-1 border-right border-dark">
                Upload Photo
              </span>
              <span class="icon-up p-1">
                <font-awesome-icon icon="upload"/>
              </span>
            </span>
            <input
              type="file"
              ref="file"
              :accept="accept"
              @change="onFileChange"
              id="new-img"
              style="display: none"
            />   
          </label>
        </div>
      </div>
      <div class="user-details">
        <div
        class="user-details__item">
          <h5>Full Name</h5>
          <article class="user-details__info">
            <p>{{ `${userObj.first_name} ${userObj.last_name}` }}</p>
            <button class="btn user-details__btn"
            @click="showForm('name')">EDIT</button>
          </article>
        </div>
        <!-- <div
        class="user-details__item">
          <h5>Address</h5>
          <article class="user-details__info">
            <p>{{ userObj.address }}</p>
            <button class="btn user-details__btn"
            @click="showForm('address')">EDIT</button>
          </article>
        </div> -->
        <div
        class="user-details__item">
          <h5>Email</h5>
          <article class="user-details__info">
            <p>{{ userObj.email }}</p>
            <button class="btn user-details__btn"
            @click="showForm('email', 'email')">EDIT</button>
          </article>
        </div>
        <div
        class="user-details__item">
          <h5>Phone</h5>
          <article class="user-details__info">
            <p>{{ userObj.phone }}</p>
            <button class="btn user-details__btn"
            @click="showForm('phone')">EDIT</button>
          </article>
        </div>
      </div>
      <button class="btn profile__trans">
        View Transaction History
      </button>
    </div>
    <!-- User Information Update Form -->
    <template v-if="showUpdateForm">
      <user-info-update-form
      @update="updateProfile"
      @close="showUpdateForm = false">
        <user-info-update-input
        :inputType="inputType"
        :inputName="selectedKey"
        :inputId="selectedKey + '-input'"
        @inputedData="getInputValue"
        >
        </user-info-update-input>
      </user-info-update-form>
    </template>
    <message-alert
    @resetAlertType="resetAlertType"
    :alertType="alertType"
    :message="alertMessage"></message-alert>
  </div>
</template>

<script>
import {
  mapMutations,
  mapActions,
  mapGetters
} from 'vuex';
import UserInfoUpdateInput from '~/components/UserInfoUpdate/UserInfoUpdateInput.vue';
import UserInfoUpdateForm from '~/components/UserInfoUpdate/UserInfoUpdateForm.vue';
import MessageAlert from '../../components/Modals/MessageAlert.vue';
export default {
  name: 'ProfilePage',
  layout: 'main',
  components: {
    UserInfoUpdateInput,
    UserInfoUpdateForm,
    MessageAlert
  },
  middleware: ['auth'],
  data () {
    return {
      alertType: '',
      alertMessage: '',
      fileError: false,
      fileErrorMsg: '',
      showUpdateForm: false,
      imgToUpload: null,
      // userObj: {
      //   name: 'John Doe',
      //   address: 'NO. 5 demo street Lagos',
      //   email: 'Johndeo.gmail.com',
      //   phone: '+123 816 805 0011'
      // },
      inputData: '',
      payload: {},
      selectedKey: '',
      inputType: 'text',
      accept: {
        default: '.jpg,.gif,.png,.jpeg,image/gif,image/jpeg,image/png',
      },
    }
  },
  computed: {
    ...mapGetters({
      userObj: 'loggedInUser'
    }),

    userImgIsNull () {
      return this.userObj.image_url === null;
    },

    isFullName () {
      return this.lastNameFeilds !== '';
    }
  },
  methods: {
    ...mapActions({
      updateUserInfo: 'updateUserInfo'
    }),

    resetAlertType () {
      this.alertType = '';
    },

    onFileChange (e) {
      this.loadingImage = true;
      let files = e.target.files || e.dataTransfer.files;
      if (files) {
        const file = files[0];
        // old 1mb file sizs ->  1048576
       if (file.size > 2097152) {
          e.preventDefault();
          this.loadingImage = false;
          this.fileError = true;
          this.fileErrorMsg = 'File is too big must be less than 1MB!'
        } else {
          this.imgToUpload = file;
          this.payload['image_url'] = file;
          this.loadingImage = false;
          this.fileError = false;
          this.updateProfile();
        }
      }
    },

    async updateProfile () {
      this.payload['id'] = this.userObj.id;
      const reqData = {};
      for (const field in this.payload) {
        if (field === 'name') {
          // Get first name and last name from full name entered.
          const splitName = this.payload.name.split(' ').slice(0, 2);
          if (splitName[0]) { reqData['first_name'] = splitName[0] };
          if (splitName[1]) { reqData['last_name'] = splitName[1] };
        } else {
          reqData[field] = this.payload[field];
        }
      }
      try {
        // Post newly updated info.
        const res = await this.updateUserInfo(reqData);
        if (res.status === 200 && res.data.hasOwnProperty('message')) {
          this.alertMessage = res.data.message;
          this.alertType = 'success';
        } else {
          this.alertMessage = res.data.message;
          this.alertType = 'danger';
        }
      } catch (error) {
        this.alertMessage = error.message;
        this.alertType = 'danger';
        console.error(error);
      }

    },

    showForm (key, type=null) {
      this.inputType = type ? type : 'text';
      this.selectedKey = key;
      this.showUpdateForm = true;
    },
  
    getInputValue (val) {
      this.payload[this.selectedKey] = val;
    }

  },
  mounted () {
    console.log(this.$auth);
  }
}
</script>

<style scoped>
.profile {
  margin: 2rem auto;
}

.icon-up {
  font-size: 1rem;
}

@media (min-width: 48.0625em) {
  .profile {
    max-width: 500px;
  }
}

.upload-img {
  width: 200px;
  margin: 3rem auto;
}

.upload-img__avatar {
  border-radius: 5px;
  height: 200px;
  width: 100%;
}

.upload-img__file {
  width: 100%;
  height: 50px;
  margin-top: 3rem;
  display: flex;
  justify-content: center;
}

@media (min-width: 48.0625em) {
  .upload-img__file {
    margin-top: 2rem;
  }
}

.upload-img__file label {
  cursor: pointer;
  font-size: 15px;
}
.d-flex {
  background-color: #e9ecef;
  color: #495057;
  border: 1px solid #495057;
  border-radius: 3px;
}
.upload-img__file input {
  display: none;
}

.user-details__info {
  display: flex;
  justify-content: space-between;
}

.user-details__btn {
  color: var(--clr-primary);
}

.profile__trans {
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
  display: block;
  margin-top: 2rem;
  width: 100%;
}
</style>