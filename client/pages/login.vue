<template>
  <div class="container">
    <template
    v-if="loginSuccess">
      <b-alert
      :show="dismissCountDown"
      variant="success"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      fade
      dismissible>{{ message }}</b-alert>
    </template>

    <template
    v-if="loginError">
      <b-alert
      :show="dismissCountDown"
      variant="danger"
      @dismissed="dismissCountDown=0"
      @dismiss-count-down="countDownChanged"
      fade
      dismissible>{{ message }}</b-alert>
    </template>

      <form
      class="login-form"
      @submit.prevent="loginUser"
      >
        <div class="form__heading row">
            <h2 class="col underline">SIGN IN</h2>
            <h2 class="col register">
                <NuxtLink
                to="/register"
                class="form__link">
                    <span>REGISTER</span>
                </NuxtLink>
            </h2>
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
            <label for="password" class="input-label">
                Password *
             </label>            
            <input 
            id="password"
            class="form__input"
            type="password"
            placeholder="Password"
            v-model="formData.password"
            required>
        </div>
        <NuxtLink
        to="#"
        class="form__link">
            Forgot Password
        </NuxtLink>
        <div class="form__group">
            <button
            class="btn from__submit"
            type="submit">
                Sign In
            </button>
        </div>
    </form>
  </div>
</template>

<script>
import { mapMutations, mapActions } from 'vuex';
export default {
    name: 'LoginPage',
    layout: 'default',

    head:{
        title: 'AgriLink | Login'
    },
  
    data () {
        return {
            dismissCountDown: 5,
            isLoginSuccessful: null,
            message: '',
            formData: {
                email: '',
                password: ''
            },
        }
    },
    computed: {
        loginSuccess () {
            return this.isLoginSuccessful;
        },
        loginError () {
            return this.isLoginSuccessful === false;
        }
    },
    methods: {
        ...mapActions({
            login: 'login'
        }),
        countDownChanged (dismissCountDown) {
          this.dismissCountDown = dismissCountDown;
        },
        showAlert () {
           this.dismissCountDown = this.dismissSecs;
        },
        async loginUser () {
            try{
                const res = await  this.$auth.loginWith('local', {
                    data: {
                        email: this.formData.email,
                        password: this.formData.password
                    },
                });
                
                // console.log(res, "lefdgupewio");
                if (res) {
                    // console.log(res);
                    this.message = res.message;
                    this.isLoginSuccessful = true;
                    // await this.$router.push('/profile')
                }
            } catch (error) {
                this.message = 'Invalid email or password';
                this.isLoginSuccessful = false;
                console.error(error.message);
                this.dismissCountDown = 5;
            }
        },
    },
    mounted () {
        // this.isLoginSuccessful = true;
    }
}
</script>

<style scoped>
    .container {
        margin-top: 3rem;
        margin-bottom: 3rem;
    }
    .form__heading h2 {
        padding: 0 15px 15px 0;
    }
    .underline {
        padding-bottom: 0.5rem;
        border-bottom: 1px solid var(--clr-primary);
    }


    @media (min-width: 48.0625em) {
        .login-form {
            max-width: 65%;
            margin: 0 auto;
        }
    }

    .login-form h2 {
        margin-bottom: 20px;
    }

    .login-form .form__group {
        margin-top: 2rem;
        margin-bottom: 0.5rem;
    }

    .form__group .input-label {
        text-transform: uppercase;
    }

    .login-form input {
        width: 100%;
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid var(--clr-base);
        border-radius: 3px;
    }

    .form__link {
        color: inherit;
        cursor: pointer;
        text-transform: uppercase;
        text-decoration: none;
    }

    .login-form button {
        width: 100%;
        padding: 10px;
        background-color: var(--clr-primary);
        color: var(--clr-ntrl-min);
        border: none;
        border-radius: 3px;
        cursor: pointer;
    }
</style>