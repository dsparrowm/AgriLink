<template>
  <div class="montly-revenue">
    <div class="monlthy-revenue__total monthly-card">
      <article class="text-center">
        <h2>$3.5 m</h2>
        <p class="monlthy-revenue__txt">
          Revenue this month
        </p>
        <div class="monlthy-revenue__bottom">
          <progress-bar :value="40">
          </progress-bar>
          <p class="monlthy-revenue__percent-value">
            <span>40%</span>
            <span>$3.6m</span>
          </p>
        </div>
      </article>
    </div>
    <div class="monlthy-revenu__by-product monthly-card">
      <product-performance-card
      :performance="revenue_by_product"
      ticks="amount">
      </product-performance-card>
    </div>
  </div>
</template>

<script>
import ProgressBar from '../../ProgressBar.vue';
import ProductPerformanceCard from '../ProductPerformanceCard.vue';
export default {
  name: 'MonthlyRevenue',
  components: {
    ProgressBar,
    ProductPerformanceCard
  },

  data () {
    return {
      revenue_by_product: [
        {productName: 'Rice', value: 10, progress: 10},
        {productName: 'Beans', value: 80, progress: 80},
        {productName: 'Eggs', value: 40, progress: 50}
      ]
    }
  }
}
</script>

<style scoped>
/* article {
  display: flex;
  flex-direction: column;
} */
.monlthy-revenue__percent-value {
  display: flex;
  font-size: var(--fs-milli);
  justify-content: space-between;
}

.monlthy-revenue__bottom {
  margin-top: auto;
}
.monlthy-revenue__bottom p {
  margin: 0;
}

</style>