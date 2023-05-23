<template>
  <footer id="AppFooter">
    <div class="footer__info">
        <div class="footer__sections">
            <h5>Contact US</h5>
            <form class="contact-form">
                <div class="form__group">
                    <label for="email-input" class="input-label">
                        Email Address
                    </label>
                    <input type="text"
                    class="form__input"
                    name="email"
                    id="email-input"
                    required>
                </div>                
                <div class="form__group">
                    <label for="message-input" class="input-label">
                        Message
                    </label>
                    <textarea
                    name="message"
                    id="message-input"
                    class="form__input"
                    rows="2"
                    required>
                    </textarea>
                </div>                
                <button 
                class="btn form__submit"
                type="submit">
                    Submit
                </button>
            </form>
        </div>
        <div class="footer__sections text-center">
            <h5>About AgriLink</h5>
            <ul class="nav">
                <li class="nav__item">
                    <NuxtLink
                    class="nav__links"
                    to="#">
                    About Us
                    </NuxtLink>
                </li>
                <li class="nav__item">
                    <NuxtLink
                    class="nav__links"
                    to="#">
                    What we do
                    </NuxtLink>
                </li>
                <li class="nav__item">
                    <NuxtLink
                    class="nav__links"
                    to="#">
                    What we do not do
                    </NuxtLink>
                </li>
            </ul>
        </div>
        <div class="footer__sections text-center">
            <h5>Terms</h5>
            <ul class="nav">
                <li class="nav__item">
                    <NuxtLink
                    class="nav__links"
                    to="#">
                    Order & checkout
                    </NuxtLink>
                </li>
                <li class="nav__item">
                    <NuxtLink
                    class="nav__links"
                    to="#">
                    Terms & Conditions
                    </NuxtLink>
                </li>
                <li class="nav__item">
                    <NuxtLink
                    class="nav__links"
                    to="#">
                    Privacy Policy
                    </NuxtLink>
                </li>
            </ul>
        </div>
    </div>
    <div class="footer__base">
        <span class="logo mr-2">Logo</span>
        <span class="copy-r icon-sm">
            <font-awesome-icon icon="copyright"/>
        </span>
    </div>
  </footer>
</template>

<script>
export default {
    name: 'AppFooter'
}
</script>

<style scoped>
    footer {
        border-top: 1px solid var(--clr-base);
    }

    .footer__info {
        background-color: var(--clr-base-dk);
        color: var(--clr-base-lt);
        display: flex;
        flex-direction: column-reverse;
        justify-content: space-between;
        gap: 2rem;
        padding: 1rem;
    }

    @media (min-width: 48.0625em) {
        .footer__info {
            flex-direction: row;
        }

    }

    .form__input {
        border-radius: 5px;
        border: none;
        display: block;
        padding: 10px;
        outline: none;
        width: 100%;
    }

    .form__submit {
        background-color: var(--clr-secondary-lt);
    }

    .nav {
        display: block;
    }

    .nav__links {
        color: inherit;
        text-decoration: none;
        cursor: pointer;
    }

    .footer__sections {
      flex: 1;
    }

    .footer__sections:nth-child(1) {
        flex: 2;
        display: none;
    }

    @media (min-width: 48.0625em) {
        .footer__sections:nth-child(1) {
            flex: 2;
            display: block;
        }
    }

    .footer__sections h5 {
        margin-bottom: 1rem;
        color: var(--clr-secondary-lt);
    }

    .footer__base {
        display: flex;
        justify-content: center;
        align-items: center;
        color: #646464;
        background-color: #000;
        border-top: 1px solid var(--clr-base);
    }

    .logo {
        border: 1.5px solid var(--clr-base);
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0 1rem;
    }

    .icon-sm {
        width: 20px;
        height: 20px;
    }
</style>