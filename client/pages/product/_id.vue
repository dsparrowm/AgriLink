<template>
  <b-container class="my-5">
    <div>
      <b-card no-body
      class="overflow-hidden">
        <b-row no-gutters>
          <b-col md="6">
            <b-card-img
            src="https://picsum.photos/400/400/?image=20" alt="Image"
            class="rounded-0">
          </b-card-img>
          </b-col>
          <b-col md="6" class="d-flex align-items-center">
            <b-card-body>
              <h3 class="text-center">PRODUCT NAME</h3>
              <b-card-text class="d-flex justify-content-between mb-0">
                <span>Price</span>
                <span>N 8, 000</span>
              </b-card-text>
              <b-card-text class="d-flex justify-content-between">
                <span>Quantity</span>
                <span>5 bags</span>
              </b-card-text>
              <b-card-text>
                <b-button
                href="/"
                class="product__btn w-100">
                  BUY Now
                </b-button>
              </b-card-text>
              <b-card-text>
                <h4 class="text-uppercase">Description</h4>
                <b-card-text class="small">
                  Lorem ipsum dolor sit amet consectetur adipisicing elit. Beatae explicabo harum sunt nemo fuga sint sed. Perspiciatis vitae amet dicta officiis enim? Debitis quidem incidunt, tempora natus ut ipsam accusantium?
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
  </div>
  </b-container>
</template>

<script>
export default {
  name: 'ProductDetails',
  layout: 'main',
  head:{
    title: 'AgriLink | Detail'
  },
}
</script>

<style scoped>

</style>