<template>
  <div class="monthly-orders">
    <div class="monthly-orders__total monthly-card">
      <h5 class="text-center title">Order Per Month</h5>
      <article>
        <h2 class="text-center">37</h2>
        <p class="text-center monthly-order__txt">
          <template v-if="increase">
            <span class="icon-md text-success">
              <font-awesome-icon icon="arrow-up"/>
            </span>
          </template>
          <template v-else>
            <span class="icon-md text-danger">
              <font-awesome-icon icon="arrow-down"/>
            </span>
          </template>
          <span :class="{
            'text-success': increase,
            'text-danger': !increase
          }">30%</span>
        </p>
        <span class="move-right">
          vs previous 30 days
        </span>
      </article>
    </div>
    <div class="monlthy-orders__by-product monthly-card">
      <product-performance-card
      :performance="orders_by_product">
      </product-performance-card>
    </div>
  </div>
</template>

<script>
import ProductPerformanceCard from '../ProductPerformanceCard.vue';
export default {
  components: { ProductPerformanceCard },
  name: 'MonthlyOrders',
  data () {
    return {
      increase: true,
      orders_by_product: [
        {productName: 'Rice', value: 10, progress: 10},
        {productName: 'Beans', value: 80, progress: 80},
        {productName: 'Eggs', value: 40, progress: 50}
      ]
    }
  }

}
</script>
<style scoped>
.monthly-orders__total .title {
  font-size: var(--fs-base);
}

.icon-md {
  font-size: var(--fs-milli);
}

article h2 {
  margin: 0;
}

.move-right {
  display: block;
  font-size: 12px;
  color: var(--clr-base-lt);
  text-align: right;
}

</style>