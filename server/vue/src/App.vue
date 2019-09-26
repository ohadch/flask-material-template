<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span class="font-weight-light">My Website Template</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn v-if="$store.authenti">
        <span class="mr-2">Logout</span>
      </v-btn>
    </v-app-bar>

    <v-content>
      <v-alert v-if="alert.message" :type="alert.type">{{alert.message}}</v-alert>
      <router-view />
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: "App",
  computed: {
    alert() {
      return this.$store.state.alert;
    }
  },
  watch: {
    $route() {
      // clear alert on location change
      this.$store.dispatch("alert/clear");
    }
  }
};
</script>
