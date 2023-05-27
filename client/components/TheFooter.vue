<template>
  <footer id="AppFooter">
    <div class="footer__info site-container">
        <div class="footer__sections">
            <h2>LOGO</h2>
            <div>
                <p class="d-flex">
                    <span class="icon-sm">
                        <font-awesome-icon icon="map-marker"/>
                    </span>
                    <span>
                        60 29th Street San Francisco, 94110 507-Union
                        Trade Center, United States America
                    </span>
                </p>
                <p class="d-flex">
                    <span class="icon-sm">
                        <font-awesome-icon icon="phone"/>
                    </span>
                    <span>
                        213-555-0468
                    </span>
                </p>
                <p class="d-flex">
                    <span class="icon-sm">
                        <font-awesome-icon icon="envelope"/>
                    </span>
                    <span>
                        contact@greenenergy.com
                    </span>
                </p>
                <div class="d-flex">
                    <p class="social-media-icons">
                        <span class="icon-md ">
                            <font-awesome-icon :icon="['fab', 'facebook']"/>
                        </span>
                    </p>
                    <p class="social-media-icons">
                        <span class="icon-md">
                            <font-awesome-icon :icon="['fab', 'twitter']"/>
                        </span>
                    </p>
                    <p class="social-media-icons">
                        <span class="icon-md">
                            <font-awesome-icon :icon="['fab', 'instagram']"/>
                        </span>
                    </p>
                    <p class="social-media-icons">
                        <span class="icon-md">
                            <font-awesome-icon :icon="['fab', 'linkedin']"/>
                        </span>
                    </p>
                </div>
            </div>
        </div>
        <div class="footer__sections modal_f">
            <h2>
                <span>
                    About AgriLink
                </span>
                <button
                @click="toggleModal('about')"
                class="modal__toggle btn">
                    <span ref="about-angle-down" class="icon-mini ml-2 rotate">
                        <font-awesome-icon icon="angle-up"/>
                    </span>
                </button>
            </h2>
            <div
            ref="about"
            class="modal__content">
                <ul class="nav-list" role="list">
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="#">
                        Social media
                        </NuxtLink>
                    </li>
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="#">
                        Checkout
                        </NuxtLink>
                    </li>
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="#">
                         SEO analysis
                        </NuxtLink>
                    </li>
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="#">
                         Promotion
                        </NuxtLink>
                    </li>
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="#">
                         About
                        </NuxtLink>
                    </li>
                </ul>
            </div>
        </div>
        <div class="footer__sections modal_f">
            <h2>
                <span>Our Mission</span>
                <button
                @click="toggleModal('mission')"
                class="modal__toggle btn">
                    <span ref="mission-angle-down" class="icon-mini ml-2 rotate">
                        <font-awesome-icon icon="angle-up"/>
                    </span>
                </button>
            </h2>
            <div
            ref="mission"
            class="modal__content">
                <ul class="nav-list" role="list">
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="/">
                        Portfolio
                        </NuxtLink>
                    </li>
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="/">
                        Contact
                        </NuxtLink>
                    </li>
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="/">
                        Privacy Policy
                        </NuxtLink>
                    </li>
                    <li class="nav__item">
                        <NuxtLink
                        class="nav__links"
                        to="/">
                        FAQ Pages
                        </NuxtLink>
                    </li>
                </ul>
            </div>
        </div>
        <div class="footer__sections modal_f">
            <h2>
                <span>
                    Newsletter
                </span>
                <button
                @click="toggleModal('newsletter')"
                class="modal__toggle btn">
                    <span ref="newsletter-angle-down" class="icon-mini ml-2 rotate">
                        <font-awesome-icon icon="angle-up"/>
                    </span>
                </button>
            </h2>
            <div ref="newsletter" class="modal__content">
                <p>
                    Subscribe To Receive Inspiration, Ideas & News In Your Inbox
                </p>
                <form class="newsletter-form">
                    <input type="text"
                    name="newsletter"
                    id="newsletter"
                    class="form__input">
                    <button
                    class="btn form__submit"
                    type="submit">
                        Subscribe
                    </button>
                </form>
            </div>
        </div>
    </div>
    <div class="footer__base">
        © 2023 All Rights Reserved. Developed By Codezeel
    </div>
  </footer>
</template>

<script>
export default {
    name: 'AppFooter',
    data () {
        return {
            showNewsletter: false,
            windowwidth: null
        }
    },

    computed : {
        windowInnerWidth: {
            get () {
                return this.windowwidth;
            },
            set (val) {
                this.windowwidth = val
            }
        }
    },

    watch: {
      windowInnerWidth (val) {
        if (val >= 1025) {
            this.showModalIfHidden ('about');
            this.showModalIfHidden ('newsletter');
            this.showModalIfHidden ('mission');
        }
      }  
    },

    methods: {
        showModalIfHidden (modalName) {
            const displayed = this.$refs[modalName].style.display;
            if (displayed === 'none') {
                this.$refs[modalName].style.display = 'block';
            }
        },
        toggleModal (modalName) {
            const displayed = this.$refs[modalName].style.display;
            if (displayed !== 'block') {
                this.$refs[modalName].style.display = 'block';
                this.$refs[modalName + '-angle-down'].classList.remove('rotate');
            } else {
                this.$refs[modalName].style.display = 'none';
                this.$refs[modalName + '-angle-down'].classList.add('rotate');
            }
        }
    },

    mounted () {
      window.addEventListener('resize', () => {
        this.windowInnerWidth = window.innerWidth;
      })
    }
}
</script>

<style scoped>
    footer {
        background-image: url('../assets/images/footer-img.jpg');
        background-repeat: no-repeat;
        background-position: center;
        background-size: cover;
        background-attachment: fixed;
    }

    .footer__info {
        color: var(--clr-ntrl-min);
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        gap: 1rem;
        padding: 1rem;
        margin: 0 auto;
    }

    /* Applies to medium screen sizes and above */
    @media (min-width: 68.0625em) {
        .footer__info {
            flex-direction: row;
            gap: 2rem;
        }

    }

    .icon-sm {
        display: inline-block;
        margin-right: 1rem;
        height: 18px;
        width: 18px;
    }

    .social-media-icons {
        background-color: #546756;
        border-radius: 50%;
        height: 50px;
        width: 50px;
        text-align: center;
        padding: .5rem 0;
        margin-right: 1rem;
    }
    .icon-md  {
        display: inline-block;
        height: 50px;
        width: 50px;
        font-size: 1.5rem;
        margin: auto 0;
    }
    .form__input {
        border-radius: 20px;
        border: none;
        display: block;
        padding: 10px;
        outline: none;
        width: 100%;
    }
    .btn {
        border: none;
        outline: none;
        background-color: inherit;
        color: inherit;
    }

    .form__submit {
        border-radius: 20px;
        background-color: var(--clr-primary);
        color: var(--clr-ntrl-min);
        margin-top: 1rem;
        padding: 1rem;
    }

    .nav__item {
       display: block;
    }

    .nav__links {
        color: var(--clr-ntrl-min);
        text-decoration: none;
        cursor: pointer;
        display: inline-block;
        width: 100%;
        padding: 0.5rem 0;
    }

    .nav__links:hover {
        color: var(--clr-primary);
    }
    .footer__sections {
      flex: 1;
    }


    .footer__sections h2 {
        display: flex;
        justify-content: space-between;
    }
    /* Applies to Medium screens and above */
    @media (min-width: 68.0625em) {
        .footer__sections h2 {
            margin-bottom: 2rem;
            margin-top: 5rem;
        }

        .modal__toggle {
            display: none; 
        }
    }

    /* Applies to Medium screens and above */
    @media (max-width: 68.0625em) {
        .modal__content {
            display: none;
        }
    }

    .rotate {
        display: block;
        transform: rotate(180deg);
    }

    .footer__base {
        color: var(--clr-ntrl-min);
        display: flex;
        justify-content: center;
        align-items: center;
        border-top: 1px solid #546756;
        padding: 3rem;
    }
</style>