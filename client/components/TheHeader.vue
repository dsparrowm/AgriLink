<template>
  <header id="AppHeader" class="site-container">
    <NuxtLink to="/" class="logo">
        Logo
    </NuxtLink>
    <div class="menu">
        <ul class="menu__list"
        :class="{
            'menu__list--show': showMenu,
            'menu__list--hide': !showMenu
        }"
        role="list">
            <template>
                <b-button @click="menuToggle"
                class="btn menu__close icon-sm">
                    <font-awesome-icon icon="times"/>
                </b-button>
            </template>
            <li
            class="menu__item"
            :class="{'menu__item--active': currentPage === 'index'}">
                <NuxtLink
                to="/"
                class="menu__link pages-links">
                    Home
                </NuxtLink>
            </li>
            <li
            class="menu__item dropdown_t"
            :class="{'menu__item--active': currentPage === 'products'}">
                <button @click="toggleSubMenu"
                class="menu__link pages-link">
                    <span 
                    class="drop_down">
                        <span class="drop_left">Products</span>
                        <span class="icon-mini ml-2 drop_right">
                            <template v-if="showSubMenu">
                                <font-awesome-icon icon="angle-up"/>
                            </template>
                            <template v-else>
                                <font-awesome-icon icon="angle-down"/>
                            </template>
                        </span>
                    </span>
                </button>
                <ul
                role="list"
                class="sub-menu products-categories"
                :class="{'sub-menu--active': showSubMenu}">
                    <li class="sub-menu__item">
                        <NuxtLink
                        to="/products"
                        class="sub-pages-links">
                        Vergitables
                        </NuxtLink>
                    </li>
                    <li class="sub-menu__item">
                        <NuxtLink
                        to="#"
                        class="sub-pages-links">
                        Vergitables
                        </NuxtLink>
                    </li>
                    <li class="sub-menu__item">
                        <NuxtLink
                        to="#"
                        class="sub-pages-links">
                        Vergitables
                        </NuxtLink>
                    </li>
                    <li class="sub-menu__item">
                        <NuxtLink
                        to="#"
                        class="sub-pages-links">
                        Vergitables
                        </NuxtLink>
                    </li>
                </ul>
            </li>
            <li
            class="menu__item"
            :class="{'menu__item--active': currentPage === 'dashboard'}">
                <NuxtLink
                to="/dashboard"
                class="menu__link pages-links">
                    Dashboard
                </NuxtLink>
            </li>
            <li
            class="menu__item"
            :class="{'menu__item--active': currentPage === 'about'}">
                <NuxtLink
                to="/about"
                class="menu__link pages-links">
                    About
                </NuxtLink>
            </li>
            <li
            class="menu__item"
            :class="{'menu__item--active': currentPage === 'support'}">
                <NuxtLink
                to="/support"
                class="menu__link pages-links">
                    Support
                </NuxtLink>
            </li>
        </ul>
    </div>
    <div class="actions">
        <button
        v-if="!isAuthenticated"
        class="btn action__login">
            <NuxtLink
            to="/register"
            class="menu__link">
                Register
            </NuxtLink>
        </button>
        <button class="btn action__avatar icon-sm">
            <NuxtLink
            v-if="!isAuthenticated"
            to="/login"
            class="menu__link">
                <font-awesome-icon icon="user"/>
            </NuxtLink>
            <NuxtLink
            v-else
            to="/profile"
            class="menu__link">
                <font-awesome-icon icon="user"/>
            </NuxtLink>
        </button>
        <button 
        @click="menuToggle"
        class="btn menu_toggle icon-sm">
            <font-awesome-icon icon="bars"/>
        </button>        
    </div>
  </header>
</template>

<script>
import { APP_PAGES } from '../utils/constants';
import { mapGetters } from 'vuex';
export default {
    name: 'AppHeader',
    data () {
        return {
            showMenu: false,
            showSubMenu: false,
            pages: APP_PAGES,
            activePage: 'index'
        }
    },
    computed: {
        ...mapGetters([
            'isAuthenticated',
            'loggedInUser'
        ]),

        currentPage : {
            get () {
                return this.activePage;
            },
            set (val) {
                this.activePage = val;
            }
        }
    },
    watch: {
        '$route.name' (val) {
            this.currentPage = val;
            this.showMenu = false;
        }
    },
    methods: {
        toggleSubMenu () {
            this.showSubMenu = !this.showSubMenu;
        },
        menuToggle () {
            this.showMenu = !this.showMenu;
        },
    },
}
</script>

<style scoped>
header {
    background-color: var(--clr-ntrl-min);
    display: flex;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 5 !important;
}

.logo {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 1rem;
}

.menu__list {
    margin: 0;
}

.icon-mini {
  display: inline-block;
  height: 0.5rem;
  width: 0.5rem;
  margin-top: -5px;
}

.menu__list--hide {
    display: none;
}
/* .menu__item {
    
} */
.dropdown_t {
    position: relative;
}
.sub-menu {
    display: none;
    min-width: 180px;
    background-color: var(--clr-ntrl-max);
    color: var(--clr-ntrl-min);
}

.sub-menu * + * {
    border-top: 1px solid var(--clr-base);
} 

/* Applies to Laptop screens and Above */
@media (min-width: 48.0625em) {
    .dropdown_t:hover .sub-menu {
        display: block;
        top: -1;
        left: 0;
        position: absolute;
    }
}

.sub-pages-links,
.pages-link,
.pages-links {
    font-weight: 500;
    font-size: 16px;
    letter-spacing: 0.1px;
    /* color: var(--clr-ntrl-min); */
}

.pages-links {
    color: var(--clr-base-dk);
}

.sub-pages-links:hover,
.pages-link:hover,
.pages-links:hover {
    color: var(--clr-primary);
}

.sub-menu__item {
    padding: 0.5rem 1rem;
    /* border-bottom: 1px solid #A9A9A9; */
}



.drop_down {
    display: flex;
    align-items: center;
}

/* Applies only to Mobile screens */
@media (max-width: 48.0625em) {
    .sub-menu {
        padding: 0 1rem;
        border-top: 1px solid var(--clr-base);
    }
    .pages-links {
        display: inline-block;
        padding: 0.5rem 0;
    }

    .pages-link {
        text-align: left;
        width: 100%;
    }
    .drop_left {
        display: inline-block;
        border-right: 1px solid var(--clr-base);
        margin-right: .5rem;
        padding: 0.5rem 0;
        width: 85%;
    }

    .sub-menu--active {
        display: block;
        position: static;
    }
}

.menu__item button {
    display: block;
    border: none;
    outline: none;
    background-color: inherit;
}

/* Applies only to Mobile screens */
@media (max-width: 48.0625em) {

    .menu__list--show {
        background-color: var(--clr-ntrl-max);
        display: block;
        position: absolute;
        top: 0;
        right: 0;
        padding: 5rem 2rem;
        width: 80vw;
        height: 100vh;
        z-index: 2;
        color: var(--clr-ntrl-min);
    }

    .menu__list--show::before {
        background-color: rgba(0,0,0,0.3);
        content: '';
        display: block;
        height: 100%;
        position: fixed;
        left: 0;
        top: 0;
        width: 20vw;
        z-index: -1;
    }
    .menu__list li + li {
        border-top: 1px solid var(--clr-base);
    }
    .menu__item {
        /* padding: 0.8rem; */
    }
}

.sub-pages-links,
.menu__link {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
}

.menu__close {
    background-color: inherit;
    border: none;
    outline: none;
    position: fixed;
    top: 1rem;
    right: 1rem;
    border-radius: 50%;
    height: 40px;
    width: 40px;
}

/* Applies to Laptop screens and Above */
@media (min-width: 48.0625em) {
    .menu__list {
        display: flex;
        gap: 1.5rem;
    }

    .menu__item--active {
        color: var(--clr-primary);
    }

    .menu__close,
    .menu_toggle {
        display: none;
    }

    .pages-link,
    .pages-links {
        display: inline-block;
        padding: 2.6em 0;
    }
}

.actions {
    display: flex;
    justify-content: center;
    align-items: center;
}

.action__login {
    background-color: var(--clr-primary);
    color: var(--clr-ntrl-min);
}
</style>