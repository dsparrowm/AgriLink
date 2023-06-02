<template>
  <div class="notifications">
    <template
    v-if="operationSucceed">
    <div class="alert_s">
      <b-alert
      :show="dismissCountDown"
      variant="success"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      fade
      dismissible>
      {{ message }}
    </b-alert>
    </div>
    </template>

    <template
      v-if="operationFailed">
    <div class="alert_e">
      <b-alert
      :show="dismissCountDown"
      variant="danger"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      fade
      dismissible>{{ message }}</b-alert>
    </div>
  </template>
  </div>
</template>

<script>
export default {
  name: 'MessageAlert',
  props: {
    message: {
      type: String,
      defualt: 'Something went wrong, Please try again',
      required: false
    },

    alertType: {
      type: String,
      defualt: '',
      required: false
    }
  },

  data () {
    return {
      isSuccessful: null,
      dismissSecs: 5,
      dismissCountDown: 0,
    }
  },

  computed: {
    operationSucceed () {
      return this.alertType === 'success' ? true : false;
    },
    operationFailed () {
      return this.alertType === 'danger' ? true : false;
    },
  },

  watch: {
    alertType (val) {
      if (val !== '') {
        this.dismissCountDown = 5;
      }
    },

    dismissCountDown (val) {
      if (val === 0) {
        this.$emit('resetAlertType');
      }
    } 
  },

  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
  }

}
</script>

<style scoped>

.notifications {
    position: fixed;
    top: 9%;
    left: 0;
    width: 100vw;
    margin: 0 auto;
    z-index: 10;
    display: flex;
    justify-content: center;
  }

  .alert_e,
  .alert_s {
    width: 70%;
    text-align: center;
  }
</style>