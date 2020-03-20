import { ContentOnly } from '../../../commons/utils/layout.utils';
import { HomeComponent } from './home/home.component';
import { CreateComponent } from './create/create.component';
import { LoginRequired } from '../../../commons/utils/auth.utils';

export const DASHBOARD_STATES: object[] = [
  {
    name: 'home',
    url: '/home',
    views: ContentOnly(HomeComponent),
    onEnter: LoginRequired
  },
  {
    name: 'create-artwork',
    url: '/create-artwork',
    views: ContentOnly(CreateComponent),
    onEnter: LoginRequired
  }
];
