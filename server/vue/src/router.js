import Vue from "vue";
import Router from "vue-router";
import HomePage from "./home/HomePage";
import LoginPage from "./login/LoginPage";
import SignUpPage from "./signup/SignUpPage";

Vue.use(Router);

export const router = new Router({
  routes: [
    {
      path: "/",
      name: "home",
      component: HomePage
    },
    {
      path: "/login",
      name: "login",
      component: LoginPage
    },
    {
      path: "/signup",
      name: "signup",
      component: SignUpPage
    },
    {
      path: "*",
      redirect: "/"
    }
  ]
});


router.beforeEach((to, from, next) => {
  // redirect to login page if not logged in and trying to access a restricted page
  const publicPages = ['/login', '/signup'];
  const authRequired = !publicPages.includes(to.path);
  const loggedIn = localStorage.getItem('user');

  if (authRequired && !loggedIn) {
    return next('/login');
  }

  next();
})
