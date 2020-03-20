import { Component, OnInit } from '@angular/core';
import { StateService } from '@uirouter/angular';

import { ArtWork } from '../../../../commons/models/artwork.models';
import { ArtWorkForm } from '../../../../commons/forms/artwork.forms';

@Component({
  selector: 'app-create',
  templateUrl: './create.component.html',
  styleUrls: ['./create.component.css']
})
export class CreateComponent implements OnInit {
  public form: ArtWorkForm;
  private images: Array<any> = [];
  constructor(
    private state: StateService
  ) { }

  ngOnInit(): void {
    this.form = new ArtWorkForm(new ArtWork());
  }

  onSubmit({value, valid}: {value: ArtWork, valid: boolean}): void {
    if (valid) {
      // send the data to the backend server
      // this.auth.login(value)
      //   .then((resp: any) => {
      //     // redirect to the dashboard
      //     this.state.go('home');
      //   })
      //   .catch((err: any) => {
      //     this.form.errors = err;
      //   })
      // ;
    }
  }

  onThumbNailsChange(event): void {
    const filesAmount = event.target.files.length;
    console.log(event.target.result);
    for (let i = 0; i < filesAmount; i++) {
      const reader = new FileReader();
      reader.onload = (event: any) => {
        console.log(event.target.result);
        this.images.push(event.target.result);
      };
      reader.readAsDataURL(event.target.files[i]);
    }
    this.form.artworkForm.patchValue({
      image: this.images
    });
  }

}
