<template>
  <v-container class="fill-height" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card class="elevation-12">
          <v-form @submit.prevent="handleSubmit" ref="form">
            <v-toolbar color="primary" dark flat>
              <v-toolbar-title>Login form</v-toolbar-title>
              <div class="flex-grow-1"></div>
            </v-toolbar>
            <v-card-text>
              <v-text-field
                label="Username"
                name="username"
                prepend-icon="person"
                type="text"
                v-model="username"
              ></v-text-field>
              <v-text-field
                v-model="password"
                id="password"
                label="Password"
                name="password"
                prepend-icon="lock"
                type="password"
                :rules="passwordRules"
              ></v-text-field>
              <v-text-field
                v-model="passwordConfirm"
                id="passwordConfirm"
                label="Confirm Password"
                name="passwordConfirm"
                prepend-icon="lock"
                type="password"
                :rules="passwordConfirmRules"
              ></v-text-field>
            </v-card-text>
            <v-card-actions>
              <router-link to="/login">
                <v-btn text color="primary">Already have an account? Sign In</v-btn>
              </router-link>
              <div class="flex-grow-1"></div>
              <v-btn :disabled="!valid" :loading="loggingIn" type="submit" color="primary">Register</v-btn>
            </v-card-actions>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "SignUpPage",
  data() {
    return {
      username: "",
      password: "",
      passwordConfirm: "",
      submitted: false,
      valid: false
    };
  },
  created() {
    // reset login status
    this.$store.dispatch("authentication/logout");
  },
  computed: {
    loggingIn() {
      return this.$store.state.authentication.status.loggingIn;
    },
    passwordRules() {
      let rules = [];

      const matchConfirm = v =>
        v == this.passwordConfirm || "Passwords must match";
      rules.push(matchConfirm);

      return rules;
    },
    passwordConfirmRules() {
      let rules = [];

      const matchConfirm = v => v == this.password || "Passwords must match";
      rules.push(matchConfirm);

      return rules;
    }
  },
  methods: {
    handleSubmit() {
      this.submitted = true;
      const { username, password } = this;
      const { dispatch } = this.$store;
      if (username && password) {
        dispatch("authentication/signup", { username, password });
      }
    },
    validateField() {
      let valid = this.$refs.form.validate();
      this.valid = valid; 
    }
  },
  watch: {
    password: "validateField",
    passwordConfirm: "validateField"
  }
};
</script>
