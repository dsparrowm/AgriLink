<template>
  <b-container class="pb-4 site-container">
    <b-form class="search-form">
      <label class="sr-only" for="inline-form-input-search">search</label>
      <b-input-group class="mb-2 mr-sm-2 mb-sm-0">
        <b-input-group-prepend>
          <b-button text="Button" class="search-form__btn filter">
            <span class="icon-sm">
              <font-awesome-icon icon="filter"/>
            </span>
          </b-button>
        </b-input-group-prepend>
        <b-form-input
        id="type-inline-form-input-search"
        type="search"
        placeholder="Search"
        v-model="searchInput">
        </b-form-input>
        <b-input-group-append>
          <b-button text="Button" class="search-form__btn search">
            <span class="icon-sm">
              <font-awesome-icon icon="search"/>
            </span>
          </b-button>
        </b-input-group-append>
      </b-input-group>
    </b-form>
    <template
      v-if="productList.length
      && !loading">
      <section>
        <b-row
        cols="1"
        cols-sm="2"
        cols-md="3"
        cols-lg="5"
        class="products">
          <b-col
          v-for="(product, i) in productList"
          :key="i"
          class="product mb-3">
          <div>
              <b-card
                no-body
                tag="article"
                class="product__card"
              >
              <b-link :href="`/product/${product.id}`"
               class="card__link">
                <div>
                  <img
                  height="200"
                  width="100%"
                  :src="getImgUrl(product.image_url)"
                  v-bind:alt="product.image_url">
                </div>
                <div class="p-2">
                  <b-card-text 
                  class="d-flex justify-content-between mb-0">
                    <b-card-text class="font-weight-bold mb-0">
                      {{ product.name }}
                    </b-card-text>
                    <b-card-text class="small text-muted">
                      &#8358;{{ product.price }}
                    </b-card-text>
                  </b-card-text>
                  <b-card-text class="mb-0 text-muted small fs-6">
                    {{product.quantity}} In stock
                  </b-card-text>
                  <b-card-text class="small mb-0">
                  {{ product.description.slice(0, 30) + '...' }}
                  <NuxtLink
                  :to="`/product/${product.id}`"
                  class="card__link text-muted small fs-6">
                    view more
                  </NuxtLink>
                  </b-card-text>
                </div>
              </b-link>
                <template #footer>
                  <template
                  v-if="userObj">                    
                  <payment
                  :product="product">
                  </payment>
                  </template>
                  <template v-else>
                    <b-button
                    href="/login"
                  class="product__btn w-100">
                    Buy Now
                  </b-button>
                  </template>
                </template>
              </b-card>
          </div>
          </b-col>
        </b-row>
      </section>
    </template>
    <template
      v-if="!productList.length
      && !loading">
        <div class="text-center w-100 p-3">
          No product found for this category.
        </div>
    </template>
    <template
      v-if="loading">
      <div class="loading text-center w-100 p-3">
        <span class="fs-1">
          <font-awesome-icon icon="spinner" />
        </span>
      </div>
      </template>
      <div
      v-if="productList.length"
      class="paging">
        <b-pagination
          v-model="currentPage"
          @change="getProductListByCategory"
          :total-rows="rows"
          :per-page="perPage"
          align="right"
        ></b-pagination> 
      </div>  
  </b-container>
</template>

<script>
import { mapActions, mapGetters } from 'vuex';
import Payment from '../../components/Payment.vue';
export default {
  components: { Payment },
  name: 'ProductListingPage',
  layout: 'main',

  head: {
    title: 'AgriLink | Products'
  },

  data () {
    return {
      loading: false,
      searchInput: '',
      currentPage: 1,
      totalItems: null,
      perPage: 12,
      productList: [],
      category: this.$route.query.category || 'all',
    }
  },

  watch: {
    '$route.query.category' (val) {
      this.category = val;
      this.getProductListByCategory();
    },
  },

  computed : {
    ...mapGetters({
      userObj: 'loggedInUser'
    }),

    rows () {
      return this.totalItems;
    }
  },

  methods : {
    ...mapActions ({
      products: 'products/productsByCategory',
    }),

    getImgUrl (url) {
      return require('../../assets/images/product_images/' + url);
    },

    async getProductListByCategory (page=1) {
      this.loading = true;

      const reqData = {
        page: page,
        per_page: this.perPage,
        category: this.category
      }
    
      try {
        const res = await this.products(reqData);
        if (res.status === 200 && !res.data.hasOwnProperty('error')) {
          this.productList = res.data.products || [];
          this.totalItems = res.data.total_items;
        } else {
          this.productList = [];
          this.totalItems = 0;
        }
        this.loading = false;
      } catch (error) {
        console.error(error);
        this.loading = false;
      }
    },    
  },
  mounted () {
    this.getProductListByCategory();
  }
}
</script>

<style scoped>
.search-form {
  width: 90%;
  margin: 2rem auto;
}

/* Applies to larger screen sizes */
@media (min-width: 48.0625em) {
  .search-form {
    width: 60%;
    margin: 3rem auto;
  }
}

.icon-sm {
  display: inline-block;
  height: 1rem;
  width: 1rem;
}

.filter, .search {
  display: flex;
  justify-content: center;
  align-items: center;
}
.search-form__btn {
  background-color: #e9ecef;
  border: 1px solid #ced4da;
  color: #495057;
}
.card__link {
  color: black;
  text-decoration: none;
}

.card__link:hover {
  color: black;
}

.product__btn {
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
  border: none;
}
</style>