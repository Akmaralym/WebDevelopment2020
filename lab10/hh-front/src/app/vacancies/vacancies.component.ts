import { Component, OnInit } from '@angular/core';
import {Vacancy} from '../models';
import {ApiService} from '../api.service';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {
  vacancies: Vacancy[];
  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.getVacancies();
  }

  getVacancies() {
    const id = this.route.snapshot.paramMap.get('id');
    this.apiService.getVacancyListOfCompany(id).subscribe(vacancies => this.vacancies = vacancies);
  }

}
