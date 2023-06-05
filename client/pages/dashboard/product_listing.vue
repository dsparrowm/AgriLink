<template>
  <div class="page-wrapper">
    <h1>Products Listing</h1>
    <b-button
    class="btn create-new-btn">
      <span class="icon-sm">
        <font-awesome-icon icon="plus"/>
      </span>
      <span>
        <NuxtLink
        to="/dashboard/add_update_product/"
        class="create-link">
        Create New
      </NuxtLink>
      </span>
    </b-button>
    <div class="products">
      <section class="products__filter">
        <b-form class="search-form">
          <label class="sr-only"
          for="inline-form-input-search">
            search
          </label>
          <b-input-group class="form-group mb-0">
            <b-form-input
            id="type-inline-form-input-search"
            type="search"
            placeholder="Search"
            class="form-field"
            v-model="searchInput">
            </b-form-input>
          </b-input-group>

          <b-input-group class="form-group mb-0">
            <b-form-select
            v-model="selectedCategory"
            :options="productCategories"
            class="form-field">
            </b-form-select>
          </b-input-group>
        </b-form>
      </section>
      <template
        v-if="productList.length
        && !loading">
        <section
        class="products__list">
          <b-row
          cols="1"
          cols-sm="2"
          cols-md="3"
          cols-lg="3">
            <b-col
            v-for="(product, i) in productList"
            :key="i"
            class="product mb-3">
            <div>
              <b-card
                    tag="article"
                    class="product__card"
                    no-body
                  >
                  <div>
                    <img
                    height="200"
                    width="100%"
                    :src="getImgUrl(product.image_url)"
                    v-bind:alt="product.image_url">
                  </div>
                  <div class="p-2">
                    <b-card-text 
                    class="mb-0">
                      <b-card-text class="mb-0">
                       {{product.name}}
                      </b-card-text>
                      <b-card-text class="mb-0 text-muted small fs-6">
                       {{product.quantity}} In stock
                      </b-card-text>
                      <b-card-text 
                      class="font-weight-bold">
                      &#8358; {{ product.price }}
                      </b-card-text>
                    </b-card-text>
                  </div>
                    <template #footer>
                      <b-card-text
                      class="d-flex justify-content-between">
                        <b-button
                        class="product__btn text-secondary font-weight-bold">
                          <span class="icon-sm mr-1">
                            <font-awesome-icon :icon="['fas', 'pen']" />
                          </span>
                          <NuxtLink
                            :to="`/dashboard/add_update_product/?ID=${product.id}`"
                            class="edit-link">
                            Edit
                          </NuxtLink>
                        </b-button>
                        <b-button
                        @click="remove(product.id)"
                        class="product__btn text-danger font-weight-bold">
                          <span class="icon-sm mr-1">
                            <font-awesome-icon icon="trash"/>
                          </span>
                          <span>
                            Delete
                          </span>
                        </b-button>
                      </b-card-text>
                      <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
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
          No Product Found.
          <NuxtLink
            to="/dashboard/add_update_product/"
            class="link">
            Create New
          </NuxtLink>
          !
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
          @change="getProductList"
          :total-rows="rows"
          :per-page="perPage"
          align="right"
        ></b-pagination>    
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
import { mapActions } from 'vuex';
import MessageAlert from '../../components/Modals/MessageAlert.vue';
import { PRODUCTS_CATEGORIES } from '../../utils/constants';
export default {
  components: { MessageAlert },
  name: 'ProductListingPage',
  layout: 'dashboard',

  head: {
    title: 'AgriLink | Products'
  },

  data () {
    return {
      alertType: '',
      alertMessage: '',
      loading: false,
      totalItems: null,
      productList: [],
      currentPage: 1,
      perPage: 12,
      selectedCategory: null,
      searchInput: '',
      def_option: { value: null, text: 'Please select Category' },
      categories: PRODUCTS_CATEGORIES
    }
  },

  // watch: {
  //   selectedCategory (val) {
  //     this.getProductList();
  //   },
  // },

  computed: {
    rows () {
      return this.totalItems;
    },

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
      farmerProductList: 'products/getFarmersProducts',
      deleteProduct: 'products/deleteProductById'
    }),

    resetAlertType () {
      this.alertType = '';
    },

    getImgUrl (url) {
      return require('../../assets/images/product_images/' + url);
    },

    async remove (ID) {
      try {
        const res = await this.deleteProduct(ID);
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
        console.error(error)
      }
    },

    async getProductList (page) {
      this.loading = true;
      const pagination = {
        page: page,
        per_page: this.perPage,
        // category: this.selectedCategory || 'all'
      }
      try {
        const res = await this.farmerProductList(pagination);
        this.productList = res.data.products || [];
        this.totalItems = res.data.total_items;
        this.loading = false;
      } catch (error) {
        console.error(error);
        this.loading = false;
      }
    },
  },

  mounted () {
    this.getProductList(this.currentPage);
  }
}
</script>

<style scoped>
.page-wrapper {
  position: relative;
}

.products {
  background-color: var(--clr-ntrl-min);
  border-radius: 5px;
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
  margin-top: 2rem;
}

.create-new-btn {
  border: none;
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
  position: absolute;
  right: 1.5rem;
  top: 2.5rem;
}

/* Applied to small and medium screen sizes */
@media (max-width: 68.0625em) {
  .products {
    margin-top: 3rem;
  }
  .create-new-btn {
    left: 1.5rem;
    top: 4rem;
  }
}

.form-field,
.product__card {
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
}

.products__filter {
  border-bottom: 1px solid #e0dfdf;
  padding: 1.5rem 2rem;
}

.search-form {
  display: flex;
  justify-content: space-between;
}

.products__list {
  padding: 2rem;
}

.product__btn {
  background-color: var(--clr-ntrl-min);
  border: none;
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
}

.icon-sm {
  font-size: 0.8rem;
}

.edit-link,
.create-link {
  color: inherit;
  text-decoration: none;
}
.notifications {
  position: fixed;
  top: 9%;
  left: 0;
  width: 100vw;
  margin: 0 auto;
  z-index: 10;
  display: flex;
  justify-content: center;
}

.alert_e,
.alert_s {
  width: 70%;
  text-align: center;
}
</style>