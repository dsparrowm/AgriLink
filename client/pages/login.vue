<template>
  <div class="container">
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
    <message-alert
    @resetAlertType="resetAlertType"
    :alertType="alertType"
    :message="alertMessage">
    </message-alert>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
import MessageAlert from '../components/Modals/MessageAlert.vue';
export default {
    components: { MessageAlert },
    name: 'LoginPage',
    layout: 'main',

    head:{
        title: 'AgriLink | Login'
    },
  
    data () {
        return {
            alertType: '',
            alertMessage: '',
            formData: {
                email: '',
                password: ''
            },
        }
    },
    watch: {
        loggedInUser (user) {
            if (user.role === 'farmer') {
                this.$router.push('/dashboard');
            } else if (user.role === 'buyer') {
                this.$router.push('/products');
            }
        }
    },
    computed: {
        ...mapGetters({
            loggedInUser: 'loggedInUser'
        }),
    },
    methods: {
        resetAlertType () {
            this.alertType = '';
        },

        async loginUser () {
            try{
                const form = new FormData();
                form.append('email', this.formData['email']);
                form.append('password', this.formData['password']);
                const res = await  this.$auth.loginWith('local', {
                    data: form,
                });

                if (res) {
                    this.alertMessage = res.message;
                    this.alertType = 'success';
                }
            } catch (error) {
                this.alertMessage = 'Invalid email or password';
                this.alertType = 'danger';
                console.error(error)
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