<template>
  <b-container>
    <div class="my-orders">
      <h1>My Orders</h1>
      <template
      v-if="orderList.length">
        <order-list-table
        :fields="fields"
        @confirm-order="updateOrderStatus"
        :table-body="orderList">
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
      <template>
      <message-alert
      @resetAlertType="resetAlertType"
      :alertType="alertType"
      :message="alertMessage">
      </message-alert>
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
import MessageAlert from '../components/Modals/MessageAlert.vue';
import OrderListTable from '../components/OrderListTable.vue';
export default {
  components: { OrderListTable, MessageAlert },
  name: 'CustomerOrderListingPage',
  layout: 'main',
  middleware: ['auth'],

  head: {
    title: 'AgriLink | My Orders'
  },

  data () {
    return {
      alertType: '',
      alertMessage: '',
      orders: [],
      fields: [
        {key: 'order_id', label: 'Order #'},
        'date',
        'amount',
        'product_name',
        'status',
        'action'
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
      userOrderList: 'products/getUserOrderlist',
      confirmOrder: 'products/confirmOrder'
    }),

    resetAlertType () {
      this.alertType = '';
    },

    async updateOrderStatus (order) {
      try {
        order.status = 'confirmed';
        const res = await this.confirmOrder({id: order.order_id});
        if (res.status === 200 && res.data.hasOwnProperty('message')) {
          this.alertMessage = res.data.message;
          this.alertType = 'success';
        } else {
          this.alertMessage = res.data.message;
          this.alertType = 'danger';
        }
        
      } catch (error) {
        this.alertMessage = error.message;
        this.alertType = 'danger';
        console.error(error);
      }
    },

    async getOrderList () {
      try {
        const res = await this.userOrderList();
        this.orders = res.Transactions;
        if (this.orders.length) {
          this.orders.map(item => {
            item.action = '';
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
</style>