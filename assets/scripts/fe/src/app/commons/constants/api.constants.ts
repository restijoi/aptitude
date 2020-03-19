import { urlsafe } from '../utils/http.utils';
import { API_URL } from './conf.constants';

/* USERS
 */
export const API_USERS = urlsafe(API_URL, 'users');

/* AUTH
 */
export const API_AUTH = urlsafe(API_USERS, 'auth');
export const API_AUTH_LOGIN = urlsafe(API_AUTH, 'login');
export const API_AUTH_REGISTER = urlsafe(API_USERS, 'register');
