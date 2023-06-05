export const strict = false;

export const state = () => ({
  auth: {
    loggedIn: null,
    user: null
  }
});

export const mutations = {};

export const actions = {
  async status (commit, payload) {
    return await this.$axios
      .get('/status')
      .then(res => {
        return res.data;
      })
      .catch(err => {
        return err;
      });
  },

  async getDashboardBalances (commit, payload) {
    return await this.$axios
      .get('/user/sales')
      .then(res => {
        return res.data;
      })
      .catch(err => {
        return err;
      });
  },

  async getSalesSummary (commit) {
    return await this.$axios
      .get('/user/sales')
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async getUserBalances (commit, ID) {
    return await this.$axios
      .get(`/user/${ID}/balance`)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  // async login (commit, payload) {
  //   const form = new FormData();
  //   // console.log(form, 'newform');
  //   return await this.$axios
  //     .post('/login', form)
  //     .then(res => {
  //       return res.data;
  //     })
  //     .catch(err => {
  //       return err;
  //     });
  // },

  async register (commit, payload) {
    const form = new FormData();
    for (const field in payload) {
      form.append(field, payload[field]);
    }
    return await this.$axios
      .post('/register', form)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  },

  async updateUserInfo (commit, payload) {
    const { id, ...data } = payload;
    const form = new FormData();
    for (const field in data) {
      form.append(field, data[field]);
    }
    return await this.$axios
      .post(`/updateUserInfo/${id}`, form)
      .then(res => {
        return res;
      })
      .catch(err => {
        return err;
      });
  }
};

export const getters = {
  isAuthenticated (state) {
    return state.auth.loggedIn;
  },

  loggedInUser (state) {
    return state.auth.user;
  }
};
