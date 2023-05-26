<template>
  <header id="AppHeader">
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
            v-for="page in pages"
            :key="page.ID"
            class="menu__item"
            :class="{'menu__item--active': page.isActive}">
                <button
                @click="goToPage(page.url)"
                class="menu__link">
                 {{ page.name }}
                </button>
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
            pages: APP_PAGES
        }
    },
    computed: {
        ...mapGetters(['isAuthenticated', 'loggedInUser'])
    },
    watch: {
        '$route.name' (val) {
            this.updateActivePage(val);
        }
    },
    methods: {
        updateActivePage (pageName) {
            if (pageName === 'index') {
                this.setActivePage('home');
            } else {
                this.setActivePage(pageName);
            }
        },
        setActivePage (pageName) {
            const activePage = this.pages
            .find(page => page.name.toLowerCase() === pageName);
            if (activePage) {
                this.pages.map(page => page.isActive = false);
                activePage.isActive = true;
            } else {
                this.pages.map(page => page.isActive = false);
            }
        },
        goToPage (page) {
            this.menuToggle();
            this.$router.push(page);
        },
        menuToggle () {
            this.showMenu = !this.showMenu;
        },
    },
    mounted () {
        this.updateActivePage(this.$route.name);
        // console.log(this.isAuthenticated, 'jsjoasjkasj')
    }
}
</script>

<style scoped>
header {
    background-color: var(--clr-ntrl-min);
    border-bottom: 1px solid var(--clr-base);
    display: flex;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 5 !important;
}

.logo {
    border: 1.5px solid var(--clr-base);
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 1rem;
}

.menu__list--hide{
    display: none;
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
        background-color: var(--clr-ntrl-min);
        display: block;
        position: absolute;
        top: 0;
        right: 0;
        width: 80vw;
        height: 100vh;
        padding: 1rem;
        z-index: 2;
    }

    .menu__list--show::before {
        background-color: rgba(0,0,0,0.5);
        content: '';
        display: block;
        height: 100%;
        position: fixed;
        left: 0;
        top: 0;
        width: 20vw;
        z-index: -1;
    }

    .menu__item {
        padding: .5rem;
        border-bottom: 1px solid var(--clr-base);
    }
}

.menu__link {
    color: inherit;
    text-decoration: none;
    cursor: pointer;
}

.menu__close {
    position: fixed;
    top: 1rem;
    left: 1rem;
    color: white;
    background-color: rgba(0,0,0,0.5);
    border-radius: 50%;
    height: 40px;
    width: 40px;
}

/* Applies to Laptop screens and Above */
@media (min-width: 48.0625em) {
    .menu {
        padding-top: 1.5rem;
    }

    .menu__list{
        display: flex;
        gap: 3rem;
        height: 100%;
    }

    .menu__item--active {
        height: 100%;
        border-bottom: 1px solid var(--clr-secondary);
        color: var(--clr-secondary);
    }

    .menu__close,
    .menu_toggle {
        display: none;
    }
}

.menu_toggle {
    border: 1px solid var(--clr-base);
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