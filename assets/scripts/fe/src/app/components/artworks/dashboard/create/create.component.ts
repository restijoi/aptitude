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

  constructor(
    private state: StateService,
    private artwork: ArtworkService
  ) { }

  ngOnInit(): void {
    this.form = new ArtWorkForm(new ArtWork());
  }

  onSubmit({ value, valid }: { value: ArtWork, valid: boolean }): void {
    if (valid) {
      this.artwork.create(this.formData)
        .then ((resp: any) => {
          console.log( resp );
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
  }

  onFeaturedImageChange(event): void {
    const featuredImage = event.target.files;
    this.formData.append('featured_image', featuredImage[0]);
  }

  onThumbNailsChange(event): void {
    const thumbnails = event.target.files;
    for (const file of thumbnails) {
      this.formData.append('image', file);
    }
  }


}
