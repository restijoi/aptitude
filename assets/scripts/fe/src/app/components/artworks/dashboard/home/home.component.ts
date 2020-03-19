import { Component, OnInit } from '@angular/core';

import { StateService } from '@uirouter/angular';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  private file: File | null = null;

  constructor(
      private state: StateService
    ) { }

  ngOnInit(): void {
  }

}
