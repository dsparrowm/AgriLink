<template>
  <div class="right-side pl-3 py-3">
    <div class="admin d-flex align-items-center mb-5">
      <div class="admin-img pl-2">
        <NuxtLink to="/profile">
          <span class="icon-sm">
            <font-awesome-icon icon="user"/>
          </span>
        </NuxtLink>
      </div>
      <div class="admin-lable ml-2 p-2">
        {{ `${user.first_name} ${user.last_name}` }}
      </div>
    </div>
    <div class="dash-menu">
      <ul role="list"
      class="dash-menu__list">
        <li class="dash-menu__item">
          <NuxtLink class="dash-menu__links dash-menu__links--active"
          to="/dashboard">
          <span class="d-flex align-items-center">
            <span class="icon-md">
              <font-awesome-icon icon="th-large"/>
            </span>
            <span>
              Dashboard
            </span>
          </span>
        </NuxtLink>
      </li>
      <li class="dash-menu__item">
        <NuxtLink class="dash-menu__links"
        to="/dashboard/product_listing">
        <span class="d-flex align-items-center">
          <span class="icon-md">
            <font-awesome-icon :icon="['fas', 'sliders-h']" />
            </span>
            <span>
              Products
            </span>
          </span>
          </NuxtLink>
        </li>
        <li class="dash-menu__item">
          <NuxtLink class="dash-menu__links"
          to="/dashboard/orders_listing">
          <span class="d-flex align-items-center">
            <span class="icon-md">
              <font-awesome-icon :icon="['fas', 'clipboard-list']" />
            </span>
            <span>
              Orders
            </span>
          </span>
          </NuxtLink>
        </li>
        <!-- <li class="dash-menu__item">
          <NuxtLink class="dash-menu__links"
          to="/transactions">
          <span class="d-flex align-items-center">
            <span class="icon-md">
              <font-awesome-icon :icon="['fas', 'exchange-alt']" />
            </span>
            <span>
              Transactions
            </span>
          </span>
          </NuxtLink>
        </li>
        <li class="dash-menu__item">
          <NuxtLink class="dash-menu__links"
          to="/transactions">
          <span class="d-flex align-items-center">
            <span class="icon-md">
              <font-awesome-icon :icon="['fas', 'bell']" />
            </span>
            <span>
              Notifications
              <span class="notify">15</span>
            </span>
          </span>
          </NuxtLink>
        </li> -->
      </ul>

    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  name: 'DashboardLeft',

  computed: {
    ...mapGetters([
      'isAuthenticated',
      'loggedInUser'
    ]),

    user () {
      return this.loggedInUser;
    }
  }
}
</script>

<style scoped>

.dash-menu {
  padding-left: 2rem;
}

@media (max-width: 68.0625em) {
  .dash-menu {
    padding: 0 2rem 0 1rem;
  }
}

.admin {
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
}

.dash-menu__links {
  color: var(--clr-base-lt);
  font-weight: 600;
  display: inline-block;
  padding: 2rem 0;
  text-decoration: none;
}

.icon-md {
  font-size: 1.5rem;
  margin-right: 1.5rem;
  transition: all 0.5s;
}

.dash-menu__links:hover {
  color: var(--clr-primary);
}

.dash-menu__links:hover .icon-md {
  transform: scale(1.5);
}

.dash-menu__links--active {
  color: var(--clr-primary);
}
.notify {
  background-color: rgb(244, 58, 25);
  border-radius: 50%;
  color: var(--clr-ntrl-min);
  font-size: 14px;
  display: inline-block;
  height: 20px;
  text-align: center;
  width: 20px;
}
</style>