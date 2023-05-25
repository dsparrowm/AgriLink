<template>
  <div class="container">
    <template
    v-if="success
    && iscountDownEnded">
      <b-alert
      :show="dismissCountDown"
      variant="success"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      fade
      dismissible>{{ message }}</b-alert>
    </template>

    <template
    v-if="error
    && iscountDownEnded">
      <b-alert
      :show="dismissCountDown"
      variant="danger"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      fade
      dismissible>{{ message }}</b-alert>
    </template>

    <h2 class="text-center">SIGN UP</h2>

    <form
    class="signup-form"
    @submit.prevent="registerUser">
    <!-- <div class="form__group">
      <label for="fname" class="input-label">
          First Name *
      </label>            
      <input
      id="fname"
      class="form__input"
      type="text"
      placeholder="First Name"
      v-model="formData.firstName"
      required>
    </div> -->
    <div class="form__group">
      <label for="lname" class="input-label">
          Name *
      </label>            
      <input
      id="lname"
      class="form__input"
      type="text"
      placeholder="Name"
      v-model="formData.name"
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
    <!-- <div class="form__group">
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
    </div> -->
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
      <div class="form__group">
        <label for="phone" class="input-label">
          Phone Number
        </label>            
        <input
        id="phone"
        class="form__input"
        type="text"
        placeholder="Phone Number"
        v-model="formData.phoneNumber"
        required>
      </div>
    </template>
    <div class="form__group">
        <button class="btn from__submit" type="submit">Sign Up</button>
    </div>
    </form>
  </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';
export default {
  name: 'RegisterPage',
  layout: 'default',
  data () {
    return {
      dismissSecs: 5,
      dismissCountDown: 0,
      formData: {
        name: '',
        // lastName: '',
        email: '',
        // phoneNumber: '',
        password: '',
        // confirmPassword: '',
        role: '',
        // location: ''
      },
      isFarmer: false,
      message: '',
      error: false,
      success: false
    }
  },
  computed: {
    iscountDownEnded () {
      return this.dismissCountDown > 0;
    }
  },
  watch: {
    'formData.role' (val) {
      this.isFarmer = val === 'farmer' ? true : false;
    }
  },
  methods: {
    ...mapActions({
      register: 'register'
    }),
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
    showAlert() {
      this.dismissCountDown = this.dismissSecs;
    },
    async registerUser () {

      try{
        const res = await this.register(this.formData);
        const user = await  this.$auth.loginWith('local', {
          data: {
            email: this.formData.email,
            password: this.formData.password
          },
        });

        if (user) {
          console.log(user, res);
          this.message = res.message;
          this.success = true;
          // await this.$router.push('/profile');
        }

      } catch (error) {
        this.message = error.message;
        this.error = true;
        console.error(error);
      }
    },
  },
  mounted () {
    console.log(this.$auth)
    // this.showAlert();
  }
}
</script>

<style scoped>
  .container {
    margin-top: 3rem;
    margin-bottom: 3rem;
  }

  @media (min-width: 48.0625em) {
    .signup-form {
      max-width: 65%;
      margin: 0 auto;
    }
  }
  .signup-form .form__group {
    margin-top: 1rem;
    /* margin-bottom: 0.5rem; */
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