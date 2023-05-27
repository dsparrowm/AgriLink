<template>
  <div class="container">
    <div class="profile">
      <div class="upload-img">
        <div class="upload-img__avatar">
          <font-awesome-icon icon="user"/>
        </div>
        <div class="upload-img__file">
          <label for="filePicker">
            <span 
            class="d-flex align-items-center justify-content-center">
              <span class="pr-1 pl-1 py-1 border-right border-dark">
                Upload Photo
              </span>
              <span class="icon-sm p-1">
                <font-awesome-icon icon="upload"/>
              </span>
            </span>
            <input
            type="file"
            name="picker"
            id="filePicker">      
          </label>
        </div>
      </div>
      <div class="user-details">
        <div
        class="user-details__item">
          <h5>Full Name</h5>
          <article class="user-details__info">
            <p>{{ userObj.name }}</p>
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
        <!-- <div
        class="user-details__item">
          <h5>Phone</h5>
          <article class="user-details__info">
            <p>{{ userObj.phone }}</p>
            <button class="btn user-details__btn"
            @click="showForm('phone')">EDIT</button>
          </article>
        </div> -->
      </div>
      <!-- {{ userObj }} -->
      <button class="btn profile__trans">
        View Transaction History
      </button>
    </div>
    <!-- User Information Update Form-->
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
export default {
  name: 'ProfilePage',
  layout: 'main',
  components: {
    UserInfoUpdateInput,
    UserInfoUpdateForm
  },
  middleware: ['auth'],
  data () {
    return {
      showUpdateForm: false,
      // userObj: {
      //   name: 'John Doe',
      //   address: 'NO. 5 demo street Lagos',
      //   email: 'Johndeo.gmail.com',
      //   phone: '+123 816 805 0011'
      // },
      inputData: '',
      payload: {},
      selectedKey: '',
      inputType: 'text'
    }
  },
  computed: {
    ...mapGetters({
      userObj: 'loggedInUser'
    }),
    isFullName () {
      return this.lastNameFeilds !== '';
    }
  },
  methods: {
    ...mapActions({
      updateUserInfo: 'updateUserInfo'
    }),

    updateProfile () {
      this.payload.ID = 0;
      this.updateUserInfo(this.payload)
    },
    showForm (key, type=null) {
      this.inputType = type ? type : 'text';
      this.selectedKey = key;
      this.showUpdateForm = true;
    },
    getInputValue (val) {
      this.payload[this.selectedKey] = val;
    }
  }
}
</script>

<style scoped>
.profile {
  margin: 2rem auto;
}

.icon-sm {
  height: 20px;
  width: 20px;
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
  display: block;
  margin-top: 2rem;
  width: 100%;
}
</style>