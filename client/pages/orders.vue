<template>
  <b-container>
    <div class="my-orders">
      <h1>My Orders</h1>
      <template
      v-if="orderList.length">
        <order-list-table
        :table-body="items">
        </order-list-table>
      </template>
      <template v-else>
        <div class="text-enter">
          No Order yet.
          <NuxtLink to="/products">
            Create one now
          </NuxtLink>
        </div>
      </template>
    </div>
  </b-container>
</template>

<script>
import {
  mapMutations,
  mapActions,
  mapGetters
} from 'vuex';
import OrderListTable from '../components/OrderListTable.vue';
export default {
  components: { OrderListTable },
  name: 'CustomerOrderListingPage',
  layout: 'main',
  middleware: ['auth'],

  head: {
    title: 'AgriLink | My Orders'
  },

  data () {
    return {
      orderList: [],
      items: [
        { ID: 40, date: '08.05.2020', ship_to: 'Dickerson', Product_Name: 'Rice', amount: 5000, status: "completed" },
        { ID: 2, date: '08.05.2020', ship_to: 'Bassey', Product_Name: 'Rice',  amount: 5000, status: "pending"},
        { ID: 3, date: '08.05.2020', ship_to: 'John', Product_Name: 'Rice',  amount: 5000, status: "pending" },
        { ID: 5, date: '08.05.2020', ship_to: 'Peter', Product_Name: 'Rice',  amount: 5000, status: "completed"},
        { ID: 7, date: '08.05.2020', ship_to: 'Paul', Product_Name: 'Rice',  amount: 5000, status: "pending"}
      ],
    }
  },

  computed: {
    ...mapGetters({
      userObj: 'loggedInUser'
    }),
  },

  methods: {
    ...mapActions({
      userOrderList: 'products/getUserOrderlist'
    }),

    async getOrderList () {
      try {
        const res = await this.userOrderList();
        this.orderList = res.Transactions;
      } catch (error) {
        console.error(error)
      }
    }
  },

  mounted () {
    this.getOrderList();
  }

}
</script>

<style scoped>
.my-orders {
  margin: 3rem auto;
}
</style>