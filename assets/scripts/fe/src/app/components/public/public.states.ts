import { ContentOnly } from '../../commons/utils/layout.utils';
// import { Disconnect } from '../../commons/utils/security.utils';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';

export const PUBLIC_STATES: object[] = [
  {
    name: 'login',
    url: '/login',
    views: ContentOnly(LoginComponent),
    params: {next: window.location.pathname}
  },
  // {
  //   name: 'register',
  //   url: '/register',
  //   views: ContentOnly(RegisterComponent),
  //   params: {next: window.location.pathname}
  // },
  // {
  //   name: 'logout',
  //   url: '/logout',
  //   onEnter: Disconnect
  // }
];
