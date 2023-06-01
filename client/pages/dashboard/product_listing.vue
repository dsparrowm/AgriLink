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
            v-model="selected"
            :options="productCategories"
            class="form-field">
            </b-form-select>
          </b-input-group>
        </b-form>
      </section>
      <section class="products__list">
      <b-row
      cols="1"
      cols-sm="2"
      cols-md="3"
      cols-lg="4">
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                      to="/dashboard/add_update_product/?ID=0"
                      class="edit-link">
                      Edit
                    </NuxtLink>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
      <b-col class="product mb-3">
      <div>
        <b-card
              img-src="https://picsum.photos/600/300/?image=25"
              img-alt="Image"
              img-top
              tag="article"
              class="product__card"
              no-body
            >
            <div class="p-2">
              <b-card-text 
              class="mb-0">
                <b-card-text class="mb-0">
                  Title
                </b-card-text>
                <b-card-text 
                class="font-weight-bold">
                 N2,000
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
                    <span>
                      Edit
                    </span>
                  </b-button>
                  <b-button
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
    </div>
    <!-- <add-or-update-modal
    :productID="0">
    </add-or-update-modal> -->
  </div>
</template>

<script>
import { PRODUCTS_CATEGORIES } from '../../utils/constants';
// import AddOrUpdateModal from '../../components/Modals/AddOrUpdateModal.vue';
export default {
  name: 'ProductListingPage',
  layout: 'dashboard',
  // components: {
  //   AddOrUpdateModal
  // },
  data () {
    return {
      selected: null,
      searchInput: '',
      def_option: { value: null, text: 'Please select Category' },
      categories: PRODUCTS_CATEGORIES
    }
  },
  computed: {
    productCategories () {
      this.categories.unshift(this.def_option);
      return this.categories;
    }
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
</style>