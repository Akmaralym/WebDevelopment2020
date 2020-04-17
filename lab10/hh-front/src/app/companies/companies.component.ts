import { Component, OnInit } from '@angular/core';
import {Company} from '../models';
import {ApiService} from '../api.service';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {
  companies: Company[];
  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies() {
    this.apiService.getCompanyList().subscribe(companies => this.companies = companies);
  }

}
