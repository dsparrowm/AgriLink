<template>
  <b-container>
    <div class="my-orders page-wrapper">
      <h1>Order Details</h1>
      <div class="order-details">
        <template
        v-if="orderList.length">
          <order-list-table
          :fields="fields"
          :table-body="orderList">
          </order-list-table>
        </template>
        <template v-else>
          <div class="text-center">
            No Order yet.
            <NuxtLink to="/products">
              Create one now
            </NuxtLink>
          </div>
        </template>
      </div>
    </div>
  </b-container>
</template>

<script>
import {
  mapMutations,
  mapActions,
  mapGetters
} from 'vuex';
import OrderListTable from '../../components/OrderListTable.vue';
export default {
  components: { OrderListTable },
  name: 'FarmersOrderListingPage',
  layout: 'dashboard',
  middleware: ['auth'],

  head: {
    title: 'AgriLink | My Orders'
  },

  data () {
    return {
      orders: [],
      fields: [
        {key: 'order_id', label: 'Order #'},
        'date',
        'amount',
        'product_name',
        'buyer_name',
        'status',
      ],
    }
  },

  computed: {
    ...mapGetters({
      userObj: 'loggedInUser'
    }),

    orderList () {
      return this.orders;
    }
  },

  methods: {
    ...mapActions({
      userOrderList: 'products/getUserOrderlist'
    }),

    async getOrderList () {
      try {
        const res = await this.userOrderList();
        this.orders = res.Transactions;
        if (this.orders.length) {
          this.orders.map(item => {
            item.date = this.$moment(item.createad_at)
            .format("DD.MM.YYYY");
          });
        }
      } catch (error) {
        console.error(error);
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
.order-details {
  background-color: var(--clr-ntrl-min);
  border-radius: 5px;
  box-shadow: 0.5px 0.5px 5px 0.5px #e0dfdf;
  margin-top: 2rem;
}
</style>