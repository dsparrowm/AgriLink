<template>
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
  >   Click To Pay
  </flutterwave-pay-button>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import {FlutterwavePayButton} from 'flutterwave-vue-v3';

export default {
  name: "Payment",
  components: { FlutterwavePayButton },

  props: {
    product: {
      type: Object,
      default: {},
      required: true,
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

    makePaymentCallback (response) {
      console.log("Payment callback", response);
      if (response.status === 'successful') {
        // send buyer id..
      }
    },

    closedPaymentModal () {
      console.log('payment modal is closed');
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