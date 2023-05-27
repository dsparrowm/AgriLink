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
    <b-row
    cols="1"
    cols-sm="2"
    cols-md="2"
    cols-lg="3"
    class="products">
      <b-col class="product mb-3">
      <div>
        <b-link href="/product/1" class="card__link">
          <b-card
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            class="product__card"
          >
          <b-card-text 
          class="d-flex justify-content-between mb-0">
            <b-card-text class="font-weight-bold mb-0">Title</b-card-text>
            <b-card-text class="small text-muted">N2,000</b-card-text>
          </b-card-text>
          <b-card-text class="small mb-0">
            Some quick example text
          </b-card-text>
            <template #footer>
              <b-button
              href="/"
              class="product__btn w-100">
                BUY Now
              </b-button>
              <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
            </template>
          </b-card>
        </b-link>
      </div>
      </b-col>
      <b-col class="product mb-3">
      <div>
        <b-link href="/product/1" class="card__link">
          <b-card
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            class="product__card"
          >
          <b-card-text 
          class="d-flex justify-content-between mb-0">
            <b-card-text class="font-weight-bold mb-0">Title</b-card-text>
            <b-card-text class="small text-muted">N2,000</b-card-text>
          </b-card-text>
          <b-card-text class="small mb-0">
            Some quick example text
          </b-card-text>
            <template #footer>
              <b-button
              href="/"
              class="product__btn w-100">
                BUY Now
              </b-button>
              <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
            </template>
          </b-card>
        </b-link>
      </div>
      </b-col>
      <b-col class="product mb-3">
      <div>
        <b-link href="/product/1" class="card__link">
          <b-card
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            class="product__card"
          >
          <b-card-text 
          class="d-flex justify-content-between mb-0">
            <b-card-text class="font-weight-bold mb-0">Title</b-card-text>
            <b-card-text class="small text-muted">N2,000</b-card-text>
          </b-card-text>
          <b-card-text class="small mb-0">
            Some quick example text
          </b-card-text>
            <template #footer>
              <b-button
              href="/"
              class="product__btn w-100">
                BUY Now
              </b-button>
              <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
            </template>
          </b-card>
        </b-link>
      </div>
      </b-col>
      <b-col class="product mb-3">
      <div>
        <b-link href="/product/1" class="card__link">
          <b-card
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            class="product__card"
          >
          <b-card-text 
          class="d-flex justify-content-between mb-0">
            <b-card-text class="font-weight-bold mb-0">Title</b-card-text>
            <b-card-text class="small text-muted">N2,000</b-card-text>
          </b-card-text>
          <b-card-text class="small mb-0">
            Some quick example text
          </b-card-text>
            <template #footer>
              <b-button
              href="/"
              class="product__btn w-100">
                BUY Now
              </b-button>
              <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
            </template>
          </b-card>
        </b-link>
      </div>
      </b-col>
      <b-col class="product mb-3">
      <div>
        <b-link href="/product/1" class="card__link">
          <b-card
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            class="product__card"
          >
          <b-card-text 
          class="d-flex justify-content-between mb-0">
            <b-card-text class="font-weight-bold mb-0">Title</b-card-text>
            <b-card-text class="small text-muted">N2,000</b-card-text>
          </b-card-text>
          <b-card-text class="small mb-0">
            Some quick example text
          </b-card-text>
            <template #footer>
              <b-button
              href="/"
              class="product__btn w-100">
                BUY Now
              </b-button>
              <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
            </template>
          </b-card>
        </b-link>
      </div>
      </b-col>
      <b-col class="product mb-3">
      <div>
        <b-link href="/product/1" class="card__link">
          <b-card
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            class="product__card"
          >
          <b-card-text 
          class="d-flex justify-content-between mb-0">
            <b-card-text class="font-weight-bold mb-0">Title</b-card-text>
            <b-card-text class="small text-muted">N2,000</b-card-text>
          </b-card-text>
          <b-card-text class="small mb-0">
            Some quick example text
          </b-card-text>
            <template #footer>
              <b-button
              href="/"
              class="product__btn w-100">
                BUY Now
              </b-button>
              <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
            </template>
          </b-card>
        </b-link>
      </div>
      </b-col>
      <b-col class="product mb-3">
      <div>
        <b-link href="/product/1" class="card__link">
          <b-card
            img-src="https://picsum.photos/600/300/?image=25"
            img-alt="Image"
            img-top
            tag="article"
            class="product__card"
          >
          <b-card-text 
          class="d-flex justify-content-between mb-0">
            <b-card-text class="font-weight-bold mb-0">Title</b-card-text>
            <b-card-text class="small text-muted">N2,000</b-card-text>
          </b-card-text>
          <b-card-text class="small mb-0">
            Some quick example text
          </b-card-text>
            <template #footer>
              <b-button
              href="/"
              class="product__btn w-100">
                BUY Now
              </b-button>
              <!-- <small class="text-muted">Last updated 3 mins ago</small> -->
            </template>
          </b-card>
        </b-link>
      </div>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  name: 'ProductListingPage',
  layout: 'default',
  
  head: {
    title: 'AgriLink | Products'
  },

  data () {
    return {
      searchInput: '',
      productListing: []
    }
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
  border: none;
}
</style>