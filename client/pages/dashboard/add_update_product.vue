<template>
  <div class="page-wrapper">
    <div class="add-update">
      <h1>
        {{ productID ? 'Update' : 'Create'}} Product
      </h1>
      <div class="add-update__modal">
        <b-form
        ref="addUpdateForm"
        @submit.prevent="submitItem"
        class="add-update__form p-3">
  
          <b-input-group
          class="form-group">
            <label
            for="product-title">
              Product title
            </label>
            <b-form-input
            id="product-name"
            type="text"
            placeholder="Enter title"
            class="form-field w-100"
            v-model="productInfo.name">
            </b-form-input>
          </b-input-group>
  
          <b-input-group class="form-group">
            <label
            for="product-price">
            Price
            </label>
            <b-form-input
            id="product-price"
            type="text"
            placeholder="Enter price"
            class="form-field w-100"
            v-model="productInfo.price">
            </b-form-input>
          </b-input-group>
  
          <b-input-group class="form-group">
            <label
            for="product-quantity">
            Quantity
            </label>
            <b-form-input
            id="product-quantity"
            type="text"
            placeholder="Enter quantity"
            class="form-field w-100"
            v-model="productInfo.quantity">
            </b-form-input>
          </b-input-group>
  
          <b-input-group class="form-group">
            <label
            for="product-desc">
              Description
            </label>
            <b-form-textarea
              id="product-desc"
              v-model="productInfo.description"
              placeholder="Enter something..."
              class="form-field w-100"
              rows="3"
              max-rows="6"
            ></b-form-textarea>
          </b-input-group>
  
          <b-input-group class="form-group">
            <label
            for="product-img">
              Image
            </label>
            <template
              v-if="fileError">
                <p class="w-100 text-danger fs-6">
                  {{ fileErrorMsg }}
                </p>
            </template>
            <div class="d-flex w-100">
              <div
              v-if="productInfo.image"
              class="uploaded-img mr-3">
                <!-- <img
                :src="productInfo.image"
                class="img-responsive"
                height="100"
                alt="New product Image"> -->
                {{ productInfo.image }}
              </div>
              <label 
              for="product-img"
              :disabled="loadingImage">
                <input
                  type="file"
                  ref="file"
                  :accept="accept"
                  @change="onFileChange"
                  id="product-img"
                  style="display: none"
                />
                <span
                class="upload-btn"
                :disabled="productInfo.image">
                  <template
                  v-if="loadingImage">
                  <font-awesome-icon
                      icon="spinner" />
                  </template>
                  <template v-else>
                    <span class="icon-md">
                      <font-awesome-icon
                      :icon="['fas', 'cloud-upload-alt']" />
                    </span>
                    <span>Upload</span>                
                  </template>
                </span>
              </label>
            </div>
          </b-input-group>
  
          <b-input-group class="form-group">
            <label
            for="product-category">
              Category
            </label>
            <b-form-select
            id="product-category"
            v-model="productInfo.category"
            :options="productCategories"
            class="form-field w-100">
            </b-form-select>
          </b-input-group>
          <button
          type="submit"
          class="btn add-update__smt">
            Submit Item
          </button>
        </b-form>
      </div>
    </div>
    <message-alert
    @resetAlertType="resetAlertType"
    :alertType="alertType"
    :message="alertMessage">
    </message-alert>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import MessageAlert from '../../components/Modals/MessageAlert.vue';
import { PRODUCTS_CATEGORIES } from '../../utils/constants';
export default {
  components: { MessageAlert },
  name: 'AddOrUpdateProductPage',
  layout: 'dashboard',

  head: {
    title: 'AgriLink | Create | Update Product'
  },

  data () {
    return {
      alertType: '',
      alertMessage: '',
      fileError: false,
      fileErrorMsg: '',
      productInfo: {
        name: '',
        description: '',
        price: '',
        image: '',
        quantity: '',
        category: ''
      },
      productID: this.$route.query.ID,
      selectedCategory: null,
      def_option: { value: null, text: 'Please select a category' },
      categories: PRODUCTS_CATEGORIES,
      accept: {
        default: '.jpg,.gif,.png,.jpeg,image/gif,image/jpeg,image/png',
      },
      loadingImage: false
    }
  },
  computed: {
    productCategories () {
      const catList = [...this.categories];
      if (catList[0].value !== null) {
        catList.unshift(this.def_option);
      }
      return catList;
    }
  },
  methods: {
    ...mapActions ({
      createProduct: 'products/createProduct',
      farmerProductList: 'products/getFarmersProducts',
      getProductById: 'products/getProductById',
      updateProductDetails: 'products/updateProductDetails',
    }),

    submitItem () {
      if (this.productID) {
        this.updateProductInfo();
      } else {
        this.createNewProduct(this.productInfo);
      }
    },

    resetAlertType () {
      this.alertType = '';
    },

    async updateProductInfo () {
      try {
        const reqDate = { ID: this.productID, ...this.productInfo };
        const res = await this.updateProductDetails(reqDate);
        if (res.status === 200 && res.data.hasOwnProperty('message')) {
          this.alertMessage = res.data.message;
          this.alertType = 'success';
          this.resetForm();
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

    async getSingleProduct (ID) {
      try {
        const res = await this.getProductById(ID);
        if (res) {
          this.productInfo.name = res.data.name;
          // this.productInfo.description = res.data.description;
          this.productInfo.price = res.data.price;
          this.productInfo.image = res.data.image_url;
          this.productInfo.quantity = res.data.quantity;
          this.productInfo.category = res.data.category;
        }
      } catch (error) {
        console.error(error);
      }
    },

    onFileChange (e) {
      this.loadingImage = true;
      let files = e.target.files || e.dataTransfer.files;
      if (files) {
        const file = files[0];
       if (file.size > 1048576) {
          e.preventDefault();
          this.loadingImage = false;
          this.fileError = true;
          this.fileErrorMsg = 'File is too big must be less than 1MB!'
        } else {
          this.productInfo.image = file;
          this.loadingImage = false;
          this.fileError = false;
        }
      }
    },

    resetForm () {
      var self = this; 
      //Iterate through each object field, key is name of the object field`
      for (const field in this.productInfo) {
        self.productInfo[field] = '';
      }
    },

    async createNewProduct () {
      try {
        const res = await this.createProduct(this.productInfo);
        if (res.status === 200 && res.data.hasOwnProperty('message')) {
          this.resetForm();
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
    }
  },

  mounted () {
    if (this.productID) {
      this.getSingleProduct(this.productID);
    }
  }
}
</script>

<style scoped>
label {
  margin-bottom: 0;
}

/* Applied to small and medium screen sizes */
@media (max-width: 68.0625em) {
  .page-wrapper {
    min-height: 100vh;
    display: grid;
    align-items: center;
  }
}

.add-update h1 {
  max-width: 500px;
  margin: 1rem auto;
}

.add-update {
  margin: 2rem 0;
}

.add-update__modal {
  background-color: var(--clr-ntrl-min);
  border-radius: 5px;
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
  max-width: 500px;
  margin: 0 auto;
}
.form-field {
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
}

.uploaded-img {
  border: 1px solid #e0dfdf;
  height: 100px;
  width: 100px;
}

.upload-btn {
  border: 1px solid #e0dfdf;
  background-color: #E6E6E6;
  color: #898585;
  height: 100px;
  width: 100px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.add-update__smt {
  border: none;
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
}
.icon-md {
  font-size: 1.5rem;
}
</style>