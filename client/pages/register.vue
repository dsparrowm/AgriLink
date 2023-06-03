<template>
  <div class="container">
    <h2 class="text-center">SIGN UP</h2>
    <form
    class="signup-form"
    @submit.prevent="registerUser">
    <div class="form__group">
      <label for="fname" class="input-label">
        First Name *
      </label>            
      <input
      id="fname"
      class="form__input"
      type="text"
      placeholder="First Name"
      v-model="formData.first_name"
      required>
    </div>
    <div class="form__group">
      <label for="lname" class="input-label">
        Last Name *
      </label>            
      <input
      id="lname"
      class="form__input"
      type="text"
      placeholder="Last Name"
      v-model="formData.last_name"
      required>
    </div>
    <div class="form__group">
      <label for="email" class="input-label">
          Email Address *
      </label>            
      <input
      id="email"
      class="form__input"
      type="email"
      placeholder="Email"
      v-model="formData.email"
      required>
    </div>
    <div class="form__group">
      <label for="phone" class="input-label">
        Phone Number
      </label>            
      <input
      id="phone"
      class="form__input"
      type="text"
      placeholder="Phone Number"
      v-model="formData.phone"
      required>
    </div>
    <div class="form__group">
      <label for="pwd-input" class="input-label">
        Password *
      </label>            
      <input
      id="pwd-input"
      class="form__input"
      type="password"
      placeholder="Password"
      v-model="formData.password"
      required>
    </div>
    <div class="form__group">
      <label for="cpwd" class="input-label">
        Confirm Password *
      </label>
      <input
      id="cpwd"
      class="form__input"
      type="password"
      placeholder="Password"
      v-model="formData.confirmPassword"
      required>
    </div>
    <div class="form__group userTypes">
      <h5>Please select a role</h5>
      <input
      type="radio"
      name="user_Type"
      id="farmer"
      value="farmer"
      v-model="formData.role"
      >
      <label for="farmer">Farmer</label>
      <input
      type="radio"
      name="user_Type"
      id="buyer"
      value="buyer"
      v-model="formData.role">
      <label for="buyer">Buyer</label>
    </div>
    <template v-if="isFarmer">
      <div class="form__group location">
        <label for="location-input" class="input-label">
          Farm Location
        </label>            
        <input
        id="location-input"
        class="form__input"
        type="text"
        placeholder="Location"
        v-model="formData.location"
        required>
      </div>
    </template>
    <div class="form__group">
        <button class="btn from__submit" type="submit">Sign Up</button>
    </div>
    </form>
    <message-alert
    @resetAlertType="resetAlertType"
    :alertType="alertType"
    :message="alertMessage">
    </message-alert>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import MessageAlert from '../components/Modals/MessageAlert.vue';
export default {
  components: { MessageAlert },
  name: 'RegisterPage',
  layout: 'main',

  head: {
    title: 'AgriLink | Register'
  },

  data () {
    return {
      alertType: '',
      alertMessage: '',
      formData: {
        first_name: '',
        last_name: '',
        email: '',
        phone: '',
        password: '',
        confirmPassword: '',
        role: '',
        location: ''
      },
      isFarmer: false,
    }
  },
  computed: {
    ...mapGetters({
        loggedInUser: 'loggedInUser'
    }),

    registerSuccess () {
      return this.isRegisterationSuccessful;
    },

    registerError () {
      return this.isRegisterationSuccessful === false;
    }
  },
  watch: {
    'formData.role' (val) {
      this.isFarmer = val === 'farmer' ? true : false;
    },
    loggedInUser (user) {
      if (user && user.role === 'farmer') {
        this.$router.push('/dashboard');
      } else {
        this.$router.push('/products');
      }
    }     
  },
  methods: {
    ...mapActions({
      register: 'register'
    }),

    resetAlertType () {
      this.alertType = '';
    },

    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },

    comparePassword () {
      if (this.formData.confirmPassword !== this.formData.password) {
        throw new Error('Passwords do not match');
      }
    },

    async registerUser () {
      try{

        this.comparePassword();

        const { confirmPassword, ...reqData} = this.formData;

        const { location, ...data } = reqData;

        const finalData = this.isFarmer ? reqData : data;

        const res = await this.register(finalData);

        if (res.status === 200) {
          const form = new FormData();
          form.append('email', this.formData['email']);
          form.append('password', this.formData['password']);
          const user = await  this.$auth.loginWith('local', {
            data: form
          });
  
          if (user) {
            this.message = res.message;
            this.isRegisterationSuccessful = true;
            this.dismissCountDown = 5;
            const newUserInfo = await this.$auth.fetchUser();
            console.log(newUserInfo);
          }
        }
      } catch (error) {
        this.message = error.message;
        this.isRegisterationSuccessful = false;
        this.dismissCountDown = 5;
      }
    },
  }
}
</script>

<style scoped>
  .container {
    margin-top: 3rem;
    margin-bottom: 3rem;
  }

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

  @media (min-width: 48.0625em) {
    .signup-form {
      max-width: 65%;
      margin: 0 auto;
    }
  }
  .signup-form .form__group {
    margin-top: 1rem;
  }
  .signup-form input[type=text],
  .signup-form input[type=password],
  .signup-form input[type=email]{
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid var(--clr-base);
    border-radius: 3px;
  }
  .form__group input[id=buyer],
  .form__group input[id=farmer]  {
    margin-right: 0.5rem;
  }
  .form__group input[id=buyer] {
    margin-left: 2rem;
  }
  input[type=text]:focus {
    border: 2px solid #555;
  }
  .signup-form button {
    width: 100%;
    padding: 10px;
    background-color: var(--clr-primary);
    color: var(--clr-ntrl-min);
    border: none;
    border-radius: 3px;
    cursor: pointer;
  }
</style>