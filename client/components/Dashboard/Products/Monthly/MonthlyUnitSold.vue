<template>
  <div class="monthly-units">
    <div class="monthly-units__total monthly-card">
      <article>
        <h2 class="text-center">16.8 k</h2>
        <p class="text-center monthly-units__txt mb-0">
          Unit sold this month
        </p>
      </article>
    </div>
    <div class="monthly-units__by-product monthly-card">
      <product-performance-card
      :performance="unit_by_product"
      ticks="unit">
      </product-performance-card>
    </div>
  </div>
</template>

<script>
import ProductPerformanceCard from '../ProductPerformanceCard.vue';
export default {
  components: { ProductPerformanceCard },
  name: 'MonthlyUnitSold',
  data () {
    return {
      unit_by_product: [
        {productName: 'Rice', value: 10, progress: 10},
        {productName: 'Beans', value: 80, progress: 80},
        {productName: 'Eggs', value: 40, progress: 50}
      ]
    }
  }

}
</script>

<style scoped>
.monthly-units__total{
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>