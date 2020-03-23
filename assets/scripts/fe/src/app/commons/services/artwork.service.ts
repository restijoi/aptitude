import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { API_ARTWORK } from '../constants/api.constants';

@Injectable({
  providedIn: 'root'
})
export class ArtworkService {

  constructor(
    private http: HttpClient,
  ) { }
    /**
     * @description create artwork
     * @param data object
     */
  async create(data: any) {
    try {
      return await this.http.post(API_ARTWORK, data)
        .toPromise();
    } catch (errors) {
      return Promise.reject(errors);
    }
  }
}
