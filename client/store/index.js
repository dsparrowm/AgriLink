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

  async login (commit, payload) {
    return await this.$axios
      .post('/login', payload)
      .then(res => {
        return res.data;
      })
      .catch(err => {
        return err;
      });
  },

  async register (commit, payload) {
    return await this.$axios
      .post('/register', payload)
      .then(res => {
        return res.data;
      })
      .catch(err => {
        return err;
      });
  },
  async updateUserInfo (commit, payload) {
    const { ID, ...data } = payload;
    return await this.$axios
      .post(`/updateUserInfo/${ID}`, data)
      .then(res => {
        return res.data;
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
