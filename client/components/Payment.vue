<template>
  <div>
    <flutterwave-pay-button
      :tx_ref="generateReference()"
      :amount="(product.price || 0).toString()"
      currency="NGN"
      payment_options="card,ussd,account"
      redirect_url=""
      class="btn payment-btn w-100"
      style=""
      :meta="{
        counsumer_id: '7898',
        consumer_mac: 'kjs9s8ss7dd'
      }"
      :customer="{
        name: `${userObj.first_name} ${userObj.last_name}`,
        email: userObj.email,
        phone_number: userObj.phone
      }"
      :customizations="{
        title: transTitle,
        description: transDesc,
        logo : 'https://flutterwave.com/images/logo-colored.svg'
      }"
      :callback="makePaymentCallback"
      :onclose="closedPaymentModal"
    >    Buy Now
    </flutterwave-pay-button>
    <template>
      <message-alert
      @resetAlertType="resetAlertType"
      :alertType="alertType"
      :message="alertMessage">
      </message-alert>
    </template>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import {FlutterwavePayButton} from 'flutterwave-vue-v3';
import MessageAlert from './Modals/MessageAlert.vue';

export default {
  name: "Payment",
  components: { 
    FlutterwavePayButton,
    MessageAlert 
  },

  props: {
    product: {
      type: Object,
      default: {},
      required: true,
    }
  },

  data () {
    return {
      isPaymentSuccessful: false,
      alertType: '',
      alertMessage: ''
    }
  },

  computed: {
    ...mapGetters({
      userObj: 'loggedInUser'
    }),

    transTitle () {
      return 'Payment Details';
    },

    transDesc () {
      return `Payment was for ${this.product.quantity} of
      ${this.product.name} by ${this.userObj.fist_name} ${this.userObj.last_name}.
      `;
    }
  },

  methods: {
    ...mapActions({
      createOrder: 'products/createOrder'
    }),

    makePaymentCallback (response) {
      // check payment status
      if (response.status === 'successful') {
        this.isPaymentSuccessful = true;
      }
    },

    resetAlertType () {
      this.alertType = '';
    },

    async createNewOrder () {
      try {
        const res = await this.createOrder({
          product_id: this.product.id
        });
        if (res.status === 200 && res.data.hasOwnProperty('message')) {
          this.alertMessage = res.data.message;
          this.alertType = 'success';
          this.$router.push('/orders');
        } else {
          this.alertMessage = res.data.error;
          this.alertType = 'danger';
        }
      } catch (error) {
        this.alertMessage = error.message;
        this.alertType = 'danger';
        console.error(error)
      }
    },

    closedPaymentModal () {
      if (this.isPaymentSuccessful) {
        // Create new order if payment succeed.
        this.createNewOrder();
      }
    },

    generateReference () {
      let date = new Date();
      return date.getTime().toString();
    }
    
  },
}
</script>

<style scoped>
.payment-btn {
  background-color: var(--clr-primary);
  color: var(--clr-ntrl-min);
  border: none;
}

</style>