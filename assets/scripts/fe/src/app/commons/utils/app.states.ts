import { PUBLIC_STATES } from '../../components/public/public.states';
import { DASHBOARD_STATES } from '../../components/artworks/dashboard/dashboard.states';

export const APP_STATES = {
  otherwise : '/login',
  states    : [].concat(
    PUBLIC_STATES,
    DASHBOARD_STATES
  )
};
