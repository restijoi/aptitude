import { urlsafe } from '../utils/http.utils';
import { API_URL } from './conf.constants';

/* USERS
 */
export const API_USERS = urlsafe(API_URL, 'users');

/**
 * ARTWORK
 */
export const API_ARTWORKS = urlsafe(API_URL, 'artworks');

/* AUTH
 */
export const API_AUTH = urlsafe(API_USERS, 'auth');
export const API_AUTH_LOGIN = urlsafe(API_AUTH, 'login');
export const API_AUTH_REGISTER = urlsafe(API_USERS, 'register');
export const API_ARTWORK = urlsafe(API_ARTWORKS, 'artwork');
