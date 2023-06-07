<template>
  <main>
    <section
    class="hero device-width">
    <b-carousel
    id="carousel-fade"
    class="carousel"
    :interval="4000"
    fade
    controls
    img-width="1024"
    img-height="480"
  >
    <b-carousel-slide
     class="sliders"
      img-src="~/assets/images/hero-img.jpg"
    >
    <div class="sliders__content">
      <h1>
        Welcome to AgriLink
      </h1>
      <p>
        Welcome to AgriLink, where we are revolutionizing the way farmers in Africa connect with buyers, both locally and internationally. Our platform is dedicated to bridging the gap between farmers and buyers, empowering communities, and fostering sustainable agricultural practices.
      </p>
      <b-button
      href="/login"
      class="hero__btn btn">
        Get Started
      </b-button>
    </div>
  </b-carousel-slide>
    <b-carousel-slide
    class="sliders"
    img-src="~/assets/images/Luscious-organic-produce.jpg"
    img-height="480"
    >
    <div class="sliders__content">
      <h1>
        AgriLink sell fresh buy fresh
      </h1>
      <p>
        
      </p>
      <b-button
      href="/login"
      class="hero__btn">
        Get Started
      </b-button>
    </div>
  </b-carousel-slide>
  </b-carousel>
    </section>
    <section class="about">
      <div class="site-container services">
        <div class="services__left">
          <img
          class="img-fluid"
          height="100%"
          width="100%"
          src="../assets/images/farm-img.jpg"
          alt="shopper">
        </div>
        <div class="services__right">
          <article>
            <h2>
              At AgriLink we bring the market to you
            </h2>
            <p class="my-3">
              We understand the challenges faced by farmers in accessing viable markets for their produce. Lack of infrastructure, limited resources, and inefficient distribution networks often hinder their ability to reach buyers who value their high-quality products. Simultaneously, buyers struggle to find reliable sources of fresh, ethically-sourced produce, especially when looking for unique offerings from Africa.
              <br/>
              Below are only but a few of what our platform offers:
            </p>
            <ul role="list">
              <li>
                <span class="icon-mini text-success mr-2">
                  <font-awesome-icon :icon="['fas', 'check-circle']" />
                </span>
                Access to fresh farm produce deliverd to your door step.
              </li>
              <li class="mt-2">
                <span class="icon-mini text-success mr-2">
                  <font-awesome-icon :icon="['fas', 'check-circle']" />
                </span>
                As a farmer you will have access to new customers across Africa from the comfort of your home.
              </li>
              <li class="mt-2">
                <span class="icon-mini text-success mr-2">
                  <font-awesome-icon :icon="['fas', 'check-circle']" />
                </span>
                Farmer Dashborad, here you get to see the performance of each product you have on display.
              </li>
            </ul>
            <b-button
            href="#"
            class="btn services__btn mt-3">
              Our About Us
            </b-button>
          </article>
        </div>
      </div>
      <div
      class="device-width about__users">
        <div class="site-container counting">
          <article class="numbers-card">
            <h2>1200</h2>
            <p>Users</p>
          </article>
          <article class="numbers-card">
            <h2>600</h2>
            <p>New Farmers</p>
          </article>
          <article class="numbers-card">
            <h2>5000</h2>
            <p>Fresh Farm Products</p>
          </article>
          <article class="numbers-card">
            <h2>1200</h2>
            <p>Buyers</p>
          </article>
        </div>
      </div>
    </section>
    <section class="daily-boom">
      <div class="site-container boom-content">
        <div class="boom-content__heading">
          <h2 class="text-center">
            Bloom Of The Day
          </h2>
          <p class="text-center">
            There are many variations of passages of Lorem Ipsum available but the majority have suffered alteration by injected humour or randomised words which don't look even slightly believable.
          </p>
        </div>
        <div>
          <b-row
          cols="1"
          cols-sm="1"
          cols-md="3"
          cols-lg="3"
          class="booms mt-4">
            <b-col>
              <b-card
                title="Best Food Supplies"
                tag="article"
                class="booms__card shadow rounded"
                img-src="../assets/images/cms-banner-1.jpg"
                img-alt="Image"
                img-height="422"
                img-top
              >
              <b-card-text class="my-3">
                Some quick example text to build on the card title and make up the bulk of the card's content.
              </b-card-text>
              <b-card-text>
                <b-link
                class="text-dark text-underline"
                href="#foo">
                  Discover More
                </b-link>
              </b-card-text>
              </b-card>
            </b-col>
            <b-col>
              <b-card
                title="Popular Dairy Products"
                tag="article"
                class="booms__card shadow rounded"
                img-src="../assets/images/cms-banner-2.jpg"
                img-alt="Image"
                img-height="422"
                img-top
              >
              <b-card-text class="my-3">
                Some quick example text to build on the card title and make up the bulk of the card's content.
              </b-card-text>
              <b-card-text>
                <b-link
                class="text-dark text-underline"
                href="#foo">
                  Discover More
                </b-link>
              </b-card-text>
              </b-card>
            </b-col>
            <b-col>
              <b-card
                title="High Quality Farm Products"
                tag="article"
                class="booms__card shadow rounded"
                img-src="../assets/images/shopper-img.jpg"
                img-alt="Image"
                img-height="422"
                img-top
              >
              <b-card-text class="my-3">
                Some quick example text to build on the card title and make up the bulk of the card's content.
              </b-card-text>
              <b-card-text>
                <b-link
                class="text-dark text-underline"
                href="#foo">
                  Discover More
                </b-link>
              </b-card-text>
              </b-card>
            </b-col>
          </b-row>
        </div>
      </div>
    </section>
    <section class="our-features">
      <div class="site-container boom-content">
        <div class="boom-content__heading">
          <h2 class="text-center">
            Enjoy Our Amazing Features
          </h2>
          <p class="text-center">
            There are many variations of passages of Lorem Ipsum available but the majority have suffered alteration by injected humour or randomised words which don't look even slightly believable.
          </p>
        </div>
        <div>
          <b-row
          cols="1"
          cols-sm="1"
          cols-md="3"
          cols-lg="3"
          class="features mt-5">
            <b-col>
              <b-card 
              class="shadow rounded text-center"
              img-src="../assets/images/market-img2.jpg"
              img-alt="Image"
              img-height="422"
              overlay>
              <button class="feature__btn">
                Fast Payment
              </button>
            </b-card>
            </b-col>
            <b-col>
              <b-card 
              class="shadow rounded text-center"
              img-src="~/assets/images/hero-img2.jpg"
              img-alt="Image"
              img-height="422"
              overlay>
              <button class="feature__btn">
                Fast Orders
              </button>
            </b-card>
            </b-col>
            <b-col>
              <b-card
              class="shadow rounded text-center"
              img-src="../assets/images/easy-to-use.jpg"
              img-alt="Image"
              img-height="422"
              overlay>
              <button class="feature__btn">
                Easy To Use
              </button>
            </b-card>
            </b-col>
          </b-row>
        </div>
      </div>
    </section>
    <section class="testimonies">
      <div class="device-width">
        <div class="wrapper boom-content__heading">
          <div class="text-slides">
            <span class="quote-icon">
              <font-awesome-icon icon="quote-right"/>
            </span>
            <p>
              Some quick example text to build on the card title and make up the bulk of the card's content. Some quick example text to build on the card title and make up the bulk of the card's content. Some quick example text to build on the card title and make up the bulk of the card's content.
            </p>
            <h4 class="mb-2">
              Maureen Biologist
            </h4>
            <span>Farmer</span>
          </div>
          <div class="slides-controles mt-2">
            <button class="slides-btn slides-btn--active"></button>
            <button class="slides-btn"></button>
            <button class="slides-btn"></button>
          </div>
        </div>
      </div>
    </section>
    <section class="our-team">
      <div class="site-container boom-content">
        <div class="boom-content__heading">
          <h2 class="text-center">
            Our Team Members
          </h2>
          <p class="text-center">
            Transparency, fairness, and sustainability are at the core of our values. We are committed to building trust and fostering long-term relationships based on mutual respect and shared success. Our team of passionate individuals brings together expertise in agriculture, technology, and business, with a common goal of making a meaningful impact on the lives of farmers and the broader agricultural community in Africa.
          </p>
        </div>
        <div>
          <div
           class="our-team-card mt-4">
              <b-card
                title="FrontEnd Dev"
                tag="article"
                class="team__card shadow rounded"
                img-src="../assets/images/team.jpeg"
                img-height="300"
                img-alt="Image"
                img-top
              >
              <b-card-text class="mt-2 font-weight-bold">
                Daniel Enagu
              </b-card-text>
              <b-card-text class="m-0">
                <span class="social-media-icons ml-2">
                  <a
                  href="https://www.linkedin.com/in/enagudaniel/"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-media-link">
                    <font-awesome-icon :icon="['fab', 'linkedin']"/>
                  </a>
                </span>
                <span class="social-media-icons ml-2">
                  <a
                  href="https://twitter.com/daniel_enagu"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-media-link">
                   <font-awesome-icon :icon="['fab', 'twitter']"/>
                  </a>
                </span>
                <span class="social-media-icons ml-2">
                  <a
                  href="https://github.com/DannyEnagu"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-media-link">
                  <font-awesome-icon :icon="['fab', 'github']" />
                  </a>
                </span>
              </b-card-text>
              </b-card>
              <b-card
                title="BackEnd Dev"
                tag="article"
                class="team__card shadow rounded"
                img-src="../assets/images/team1.jpeg"
                img-height="300"
                img-alt="Image"
                img-top
              >
              <b-card-text class="mt-2 font-weight-bold">
                Davies Aniefiok
              </b-card-text>
              <b-card-text class="m-0">
                <span class="social-media-icons ml-2">
                  <a href="https://www.linkedin.com/in/davies-aniefiok"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-media-link">
                      <font-awesome-icon :icon="['fab', 'linkedin']"/>
                  </a>
                </span>
                <span class="social-media-icons ml-2">
                  <a href="http://twitter.com/dsparrowm"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-media-link">
                  <font-awesome-icon :icon="['fab', 'twitter']"/>
                  </a>
                </span>
                <span class="social-media-icons ml-2">
                  <a href="http://github.com/dsparrowm"
                  target="_blank"
                  rel="noopener noreferrer"
                  class="social-media-link">
                   <font-awesome-icon :icon="['fab', 'github']" />
                  </a>
                </span>
              </b-card-text>
              </b-card>
          </div>
        </div>
      </div>
    </section>
    <section class="contact">
      <div class="contact__empty"></div>
      <b-form class="contact__form shadow rounded">
        <h2 class="text-center">Get In Touch</h2>
        <p class="text-center">
          Contact us today to learn more about how you can be part of this exciting movement. Together, we can cultivate a brighter tomorrow.
        </p>
        
        <b-input-group
          class="form-group d-flex">
            <b-form-input
            id="full-name"
            type="text"
            placeholder="Your Full Name"
            class="form-field mr-3"
            required>
            </b-form-input>
            <b-form-input
            id="email"
            type="email"
            placeholder="Your Email Address"
            class="form-field"
            required>
            </b-form-input>
        </b-input-group>
        <b-input-group class="form-group">
          <b-form-textarea
            id="message"
            placeholder="Write Your Message"
            class="form-field w-100"
            rows="3"
            max-rows="6"
            required
          ></b-form-textarea>
          </b-input-group>
          <button
          type="submit"
          class="btn contact__btn w-100">
            Get In Touch
          </button>
      </b-form>
    </section>
  </main>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';
export default {
  name: 'IndexPage',
  layout: 'main',

  head:{
    title: 'AgriLink | Home',
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
.icon-mini {
  font-size: var(--fs-base);
}
.text-underline {
  text-decoration: underline;
}
.text-underline:hover {
  color: var(--clr-primary) !important;
}


.btn {
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
  border: none;
  border-radius: 30px;
  padding: 1rem 2rem;
}

@media (max-width: 68.0625em) {
  .btn {
    padding: 0.5rem 2rem;
  }
}

.sliders >>> .carousel-caption {
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  display: flex;
  align-items: center;
  background: rgba(57, 57, 57, 0.5);
}

.sliders__content {
  text-align: left;
  max-width: 800px;
  margin: 0 15%;
  transform: all;
}


h1, h2 {
  font-weight: 700;
  font-size: var(--fs-kilo);
  letter-spacing: -0.3px;
}

@media (max-width: 68.0625em) {
  h1, h2 {
    font-weight: 500;
    font-size: var(--fs-h1);
  }
}

@media (max-width: 0.032em) {
  h1, h2 {
    font-size: var(--fs-h6);
  }
}

.services {
  margin-top: 150px;
  margin-bottom: 150px;
  display: flex;
  align-items: center;
  gap: 3rem;
}

@media (max-width: 68.0625em) {
  .services {
    margin-top: 100px;
    margin-bottom: 100px;
    flex-direction: column-reverse;
    align-items: center;
  }
}

.services__right,
.services__left {
  width: 50%;
}

@media (max-width: 68.0625em) {
  .services__right,
  .services__left {
    width: 100%;
  }
}

.services__left img {
  border-radius: 20px;
}
.contact__empty,
.about__users {
  background-color: var(--clr-primary-dkr);
  background-image: url('../assets/images/testimonial-parallax.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  color: var(--clr-ntrl-min);
  min-height: 300px;
}

.counting {
  align-items: center;
  display: flex;
  margin-top: auto;
  margin-bottom: auto;
  min-height: inherit;
}

.counting > * + * {
  border-left: 1px solid #5d6f56;
}

.numbers-card {
  width: 25%;
  text-align: center;
}
.numbers-card h2 {
  color: var(--clr-primary);
  margin-bottom: 0;
}

.numbers-card p {
  font-family: "Averia Sans Libre", Sans-serif;
  font-size: 30px;
  font-weight: 400;
  line-height: 45px;
  letter-spacing: -0.3px;
  margin: 0;
  padding: 0;
}

@media (max-width: 68.0625em) {
  .counting {
    flex-direction: column;
    align-items: center;
    padding: 3rem;
  }
  .counting > * + * {
    border-left: 0;
    margin-top: 2rem;
  }
  .numbers-card  {
    width: 100%;
  }
}

.boom-content {
  margin-top: 150px;
  margin-bottom: 150px;
}

.boom-content__heading {
  max-width: 800px;
  margin: 0 auto;
}

.booms__card >>> .card-title {
  font-weight: 700;
  font-size: 30px;
  line-height: 1.2;
  letter-spacing: -0.3px;
  text-transform: capitalize;
  margin-bottom: 0.75rem;
}

.our-team-card >>> .card-title {
  font-size: var(--fs-base);
  text-transform: capitalize;
  margin-bottom: 0.75rem;
}

.feature__btn {
  border: none;
  outline: none;
  background-color: var(--clr-ntrl-min);
  font-family: "Averia Sans Libre", Sans-serif;
  font-size: 30px;
  font-weight: 700;
  line-height: 37px;
  letter-spacing: -0.3px;
  color: var(--clr-ntrl-max);
  border-radius: 40px 40px 40px 40px;
  padding: 19px 30px 19px 30px;
  margin-top: auto;
}

.feature__btn:hover {
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
}

@media (max-width: 68.0625em) {
  .booms > * + *,
  .features > * + * {
    margin-top: 2rem;
  }
}

.testimonies {
  background-color: var(--clr-primary-dkr);
  background-image: url('../assets/images/testimonial-parallax.jpg');
  background-position: center center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  text-align: center;
  color: var(--clr-ntrl-min);
  padding: 1rem;
}

.wrapper {
  padding: 100px 0;
}
.quote-icon {
  color: var(--clr-primary);
  font-size: var(--fs-giga);
  font-weight: 700;
  line-height: 37px;
  display: inline-block;
  margin-bottom: 1.5rem;
}

.slides-btn {
  background-color: var(--clr-primary-dkr);
  border: none;
  display: inline-block;
  outline: none;
  border-radius: 50%;
  height: 10px;
  width: 10px;
}

.slides-btn--active {
  background-color: var(--clr-primary) !important;
}
.our-team-card  {
  display: flex;
  justify-content: center;
  gap: 2rem;
}

@media (max-width: 68.0625em) {
  .our-team-card {
    flex-direction: column;
    align-items: center;
  }
}

.team__card {
  max-width: 350px;
}

.social-media-link  {
  text-decoration: none;
  color: var(--clr-ntrl-max);
  font-size: 1.5rem;
}

.social-media-link:hover {
  color: var(--clr-primary);
}

.contact__form {
  padding: 40px 30px 40px 30px;
  margin-top: -80px;
  margin-bottom: 100px;
  background-color: var(--clr-ntrl-min);
  max-width: 50%;
  margin-left: auto;
  margin-right: auto;
  z-index: 5;
}

.form-field {
  padding: 2rem;
  border: none;
  border-radius: 30px;
  display: inline-block;
  background-color: aliceblue;
}

@media (max-width: 500px) {
  .contact__form {
    min-width: 100%;
    margin-left: 0;
    margin-right: 0;
  }

  .form-field {
    padding: 1rem;
    font-size: 14px;
  }
}

</style>