import { Component, OnInit } from '@angular/core';
import { StateService } from '@uirouter/angular';

import { ArtworkService } from '../../../../commons/services/artwork.service';
import { ArtWork } from '../../../../commons/models/artwork.models';
import { ArtWorkForm } from '../../../../commons/forms/artwork.forms';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {
  public form: ArtWorkForm;
  private formData: FormData = new FormData();
  public featuredImage: File[] = [];
  public ThumbnailImage: File[] = [];

  constructor(
    private state: StateService,
    private artwork: ArtworkService
  ) { }

  ngOnInit(): void {
    this.form = new ArtWorkForm(new ArtWork());
  }

  onSubmit({ value, valid }: { value: ArtWork, valid: boolean }): void {
    // save the thumbnail in formData
    for (const file of this.ThumbnailImage) {
      this.formData.append('image', file);
    }

    if (valid) {
      this.artwork.create(this.formData)
        .then ((resp: any) => {
          console.log( resp );
          alert("added successfully");
          this.state.go('home');
        })
        .catch( (error: any ) => {
          console.log( error );
        })
      ;
    }
  }

  onFormChange(event): void {
    if (!!event.target.id) {
      const id = event.target.id;
      const value = this.form.artworkForm.get(id).value;
      this.formData.append(id, value);
    }
    
    if (event.target.id == 'is_free') {
      this.form.artworkForm.get('price').setValue(null);
      this.formData.delete("price");
    }

  }

  onFeaturedImageChange(event): void {
    this.featuredImage.push(...event.addedFiles);
    this.formData.append('featured_image', this.featuredImage[0]);
    console.log(this.formData.get("featured_image"));
  }

  onFeaturedImageRemove(event) {
    this.formData.delete("featured_image");
    this.featuredImage.splice(this.featuredImage.indexOf(event), 1);
  }

  onThumbNailsChange(event): void {
    this.ThumbnailImage.push(...event.addedFiles);
  }

  onThumbNailsRemove(event) {
    this.ThumbnailImage.splice(this.ThumbnailImage.indexOf(event), 1);
  }
}
