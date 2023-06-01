<template>
  <div class="add-update">
    <div class="backdrop">
      <div class="add-update__modal">
        <b-form class="add-update__form">
  
          <b-input-group class="form-group">
            <label
            for="product-title">
            product title
            </label>
            <b-form-input
            id="product-name"
            type="text"
            placeholder="Enter title"
            class="form-field"
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
            class="form-field"
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
            class="form-field"
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
              rows="3"
              max-rows="6"
            ></b-form-textarea>
          </b-input-group>
  
          <b-input-group class="form-group">
            <label
            for="product-img">
              Image
            </label>
            <div>
              <img
              v-if="productInfo.imag"
              :src="productInfo.image"
              class="img-responsive"
              height="100"
              alt="New product Image">
            </div>
            <input
              type="file"
              ref="file"
              :accept="accept"
              @change="onFileChange"
              id="product-img"
              style="display: none"
            />
            <button
              type="reset"
              class="btn btn-primary"
              :disabled="loadingImage"
              @click="selectFile"
              >
              Choose File
            </button>
          </b-input-group>
  
          <b-input-group class="form-group">
            <label
            for="product-category">
              Category
            </label>
            <b-form-select
            id="product-category"
            v-model="selectedCategory"
            :options="productCategories"
            class="form-field">
            </b-form-select>
          </b-input-group>
        </b-form>
      </div>
    </div>
  </div>
</template>

<script>
import { PRODUCTS_CATEGORIES } from '../../utils/constants';
export default {
  name: 'AddOrUpdateModal',
  props: {
    productID: {
      type: Number,
      require: true,
      default: 0
    }
  },
  data () {
    return {
      productInfo: {
        name: '',
        description: '',
        price: '',
        image: '',
        quantity: ''
      },
      selectedCategory: null,
      def_option: { value: null, text: 'Please select Category' },
      categories: PRODUCTS_CATEGORIES,
      accept: {
        default: '.jpg,.gif,.png,.jpeg,image/gif,image/jpeg,image/png',
      },
      loadingImage: false
    }
  },
  computed: {
    productCategories () {
      this.categories.unshift(this.def_option);
      return this.categories;
    }
  },
  methods: {
    selectFile () {
      // this.$refs.file
      console.log(this.$refs.file)
    },
    onFileChange () {
      console.log('Yes I was called');
    }
  }
}
</script>
