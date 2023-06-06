<template>
  <main>
    <section
    class="hero device-width">
    <b-carousel
    id="carousel-fade"
    class="carousel"
    style="text-shadow: 0px 0px 2px #000"
    :interval="3000"
    fade
    controls
    img-width="1024"
    img-height="480"
  >
    <b-carousel-slide
     class="sliders"
      img-src="https://picsum.photos/1024/480/?image=10"
    >
    <div class="sliders__content">
      <h1>
        Welcome to AgriLink
      </h1>
      <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Earum accusantium alias dolore animi voluptatum placeat velit officia! Suscipit distinctio autem recusandae quos deleniti, debitis voluptatibus earum iusto vitae minus facilis!
      </p>
      <b-button
      href="/login"
      class="hero__btn">
        Get Started
      </b-button>
    </div>
  </b-carousel-slide>
    <b-carousel-slide
    class="sliders"
      img-src="https://picsum.photos/1024/480/?image=12"
    >
    <div class="sliders__content">
      <h1>Hello world!</h1>
    </div>
  </b-carousel-slide>
  </b-carousel>
    </section>
  </main>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';
export default {
  name: 'IndexPage',
  layout: 'main',

  head:{
    title: 'AgriLink | Home'
  },

  methods: {
    ...mapActions({
      status: 'status',
    }),
  },
  mounted () {
    this.status();
  }
}
</script>

<style scoped>
.sliders {
  position: relative;
  border: 1px solid red;
}

.sliders >>> .carousel-caption {
  top: 20px;
  border: 2px solid red;
  text-align: left;
  display: flex;
  align-items: center;
}
.hero__btn {
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
  border: none;
  border-radius: 30px 30px 30px 30px;
  border-radius: 20px;
  margin-top: 2rem;
  padding: 1rem 2rem;
}

.sliders__content {
  transform: all;
}

.sliders__content h1 {
  font-weight: 700;
  font-size: var(--fs-kilo);
  line-height: 70px;
  letter-spacing: -0.3px;
}


/* .sliders__content {
  position: absolute;
  top: 25%;
  left: 10%;
  border: 1px solid black;
  width: 500px;
  text-align: left;
} */
</style>

