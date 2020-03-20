/**
 * Model class for signin in
 */
export class ArtWork {
  featured_image?: File = null;
  title: string = null;
  description: string = null;
  image?: File = null;
  is_free: string = null;
  price: string = null;

  constructor(data = {}) {
      Object.assign(this, data);
  }
}
