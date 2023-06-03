<template>
  <b-container class="my-5">
    <div
    v-if="product">
      <b-card no-body
      class="overflow-hidden shadow">
        <b-row no-gutters>
          <b-col
          v-if="product.image_url"
          md="6">
            <b-card-img
            :src="getImgUrl(product.image_url)"
            v-bind:alt="product.name"
            class="rounded-0">
          </b-card-img>
          </b-col>
          <b-col 
          md="6" 
          class="d-flex align-items-center">
            <b-card-body>
              <h3 class="text-center text-uppercase">
                {{ product.name }}
              </h3>
              <b-card-text class="d-flex justify-content-between mb-0">
                <span>Price</span>
                <span> &#8358; {{ product.price }} </span>
              </b-card-text>
              <b-card-text class="d-flex justify-content-between">
                <span>Quantity</span>
                <span>{{product.quantity}} In stock</span>
              </b-card-text>
              <b-card-text>
                <b-button
                href="/"
                class="product__btn buy-now-btn w-100">
                  Buy Now
                </b-button>
              </b-card-text>
              <b-card-text>
                <h4 class="text-uppercase">Description</h4>
                <b-card-text class="small">
                  {{ product.description }}
                </b-card-text>
                <h4 class="text-uppercase">About Farmer</h4>
                <b-card-text class="mb-0">
                  <span>name</span>
                  <span>John Doe</span>
                </b-card-text>
                <b-card-text class="mb-0">
                  <span>Farm Location</span>
                  <span>No. 10 fake Street, Lagos Nigeria</span>
                </b-card-text>
                <b-card-text class="mb-0">
                  <span>Contact Details</span>
                  <span>+234 816 5555 892</span>
                </b-card-text>
              </b-card-text>
            </b-card-body>
          </b-col>
        </b-row>
    </b-card>
    <!-- <img src="../../assets/images/product_images" alt=""> -->
  </div>
  </b-container>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
export default {
  name: 'ProductDetails',
  layout: 'main',
  head:{
    title: 'AgriLink | Product Details'
  },

  data () {
    return {
      product: {},
      productId: this.$route.params.id,
      productOwner: {} 
    }
  },
  methods: {
    ...mapActions ({
      getProductById: 'products/getProductById',
    }),

    getImgUrl (url) {
      return require('../../assets/images/product_images/' + url);
    },

    async getSingleProduct () {
      try {
        const res = await this.getProductById(this.productId);
        if (res) {
          this.product = res.data;
          // this.product.description = res.data.description;
        }
      } catch (error) {
        console.error(error);
      }
    },
  },

  mounted () {
    this.getSingleProduct();
  }
}
</script>

<style scoped>

.buy-now-btn {
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
  border: none;
}

</style>