<template>
  <div class="wrapper">
    <div class="dashboard">
      <template v-if="showBars">
        <button @click="toggleLeftSideMenu"
        class="btn icon-md">
          <font-awesome-icon icon="bars"/>
        </button>
      </template>
      <template v-else>
        <button @click="toggleLeftSideMenu"
         class="btn icon-md hide">
          <font-awesome-icon icon="times"/>
        </button>
      </template>
      <div ref="dashboard-left" class="dashboard-left">
        <dashboard-left></dashboard-left>
      </div>
      <div class="dashboard-main">
        <Nuxt />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DashboardLayout',

  data () {
    return {
      showBars: true
    }
  },

  methods : {
    toggleLeftSideMenu () {
      const leftSideClassesList = [...this.$refs['dashboard-left'].classList];
      if (leftSideClassesList.includes('dashboard-left--show')) {
        this.$refs['dashboard-left'].classList.remove('dashboard-left--show');
        this.showBars = true;
      } else {
        this.$refs['dashboard-left'].classList.add('dashboard-left--show');
        this.showBars = false;
      }
    }
  }
}
</script>

<style scoped>
.dashboard {
  display: grid;
  grid-template-columns: 250px 1fr;
  background-color: var(--clr-ntrl-min);
  color: var(--clr-base);
  height: 100vh;
  position: relative;
}

.icon-md {
  display: none;
  font-size: 1.5rem;
  position: absolute;
  right: 1rem;
  top: 0.5rem;
  z-index: 6;
}

.dashboard-left  {
  /* border-right: 2px solid black; */
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
}

/* Applyed to mobile screen sizes */
@media (max-width: 68.0625em) {
  .dashboard {
    grid-template-columns: 1fr;
  }
  .icon-md {
    display: block;
  }
  .dashboard-left {
    position: absolute;
    left: 0;
    top: 0;
    background-color: var(--clr-ntrl-min);
    height: 100%;
    z-index: 5;
    transition: all 0.3s;
    transform: translateX(-250px);
  }
  .dashboard-left--show {
    transform: translateX(0px);
  }
}
</style>