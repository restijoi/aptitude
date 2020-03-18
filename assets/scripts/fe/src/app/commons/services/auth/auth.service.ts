import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

import { API_AUTH_LOGIN, API_AUTH } from '../../constants/api.constants';
import { AUTH_KEY } from '../../constants/conf.constants';
// import { User } from '../../models/user.models';


@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient,
    private cookie: CookieService
  ) { }

  async login(data: any) {
    try {
      const resp = await this.http.post(API_AUTH_LOGIN, data)
        .toPromise();
      this.setToken(resp);
      return resp;
    } catch (errors) {
      return Promise.reject(errors);
    }
  }

  /**
   * MANAGE USER TOKEN
   * @desc:  manage user token generated from the backend
   * to be used on authenticated requests
   */
  setToken(token: any): void {
    // save the generated token to the local storage
    this.cookie.set(AUTH_KEY, JSON.stringify(token));
    // (window as any).localStorage[AUTH_KEY] = JSON.stringify(token);
  }

  getToken(): string {
    // fetch the generated token from the storage
    const token = this.cookie.get(AUTH_KEY);
    if (!token) {
      return null;
    }
    return JSON.parse(token);
  }

  rmToken(): void {
    // clear the token from the local storage.
    this.cookie.delete(AUTH_KEY);
  }

  authenticated() {
    return this.getToken() ? true : false;
  }

  async setUser() {
    // const resp = await this.http.get(API_AUTH)
    //   .toPromise();
    // this.user = new User(resp);
  }

  getUser() {
    // if (this.user.id === null) {
    //   this.setUser();
    // }
    // return this.user;
  }
}
