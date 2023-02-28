import React, { useState, useContext } from "react";
import { Context } from "../store/appContext";
import { Link } from "react-router-dom";

export const Flight_offers = () => {
  return (
    <>
      <h1>Elige tu vuelo</h1>
      <div class="continer-sm">
        <div class="container-sm border border-dark border border-2">
          <h3>Locacion</h3>
          <div class="row">
            <div class="col-sm">
              <div class="mb-2">
                <label id="origin-label" for="origin-input" class="form-label">
                  Origen
                </label>
                <div class="input-group">
                  <span class="input-group-text">
                    <i class="bi-pin-map"></i>{" "}
                  </span>
                  <input
                    type="text"
                    class="form-control"
                    list="origin-options"
                    id="origin-input"
                    placeholder="Location"
                    aria-describedby="origin-label"
                  />
                  <datalist id="origin-options"></datalist>
                </div>
              </div>
            </div>
            <div class="col-sm">
              <div class="mb-2">
                <label
                  id="destination-label"
                  for="destination-input"
                  class="form-label"
                >
                  Destino
                </label>
                <div class="input-group">
                  <span class="input-group-text">
                    <i class="bi-pin-map-fill"></i>{" "}
                  </span>
                  <input
                    type="text"
                    class="form-control"
                    list="destination-options"
                    id="destination-input"
                    placeholder="Location"
                    aria-describedby="destination-label"
                  />
                  <datalist id="destination-options"></datalist>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* <!--  --> */}
        <div class="container-sm d-flex align-content-start">
          <div class="row">
            <div class="mb-2 col">
              <div class="h-100 card">
                <div class="card-body">
                  <h5 class="card-title">Dates</h5>
                  <div class="mb-2">
                    <label
                      id="flight-type-label"
                      for="flight-type-select"
                      class="form-label"
                    >
                      Flight
                    </label>
                    <select
                      id="flight-type-select"
                      class="form-select"
                      aria-describedby="flight-type-label"
                    >
                      <option value="one-way">One-way</option>
                      <option value="round-trip">Round-trip</option>
                    </select>
                  </div>
                  <div id="departure-date" class="mb-2">
                    <div id="departure-date" class="mb-2">
                      <label
                        id="departure-date-label"
                        for="departure-date-input"
                        class="form-label"
                      >
                        Departure date
                      </label>
                      <div class="input-group">
                        <span class="input-group-text">
                          <i class="bi-calendar"></i>
                        </span>
                        <input
                          type="date"
                          class="form-control"
                          id="departure-date-input"
                          aria-describedby="departure-date-label"
                        />
                      </div>
                    </div>
                  </div>
                  <div id="return-date" class="mb-2">
                    <div id="return-date" class="mb-2">
                      <label
                        id="return-date-label"
                        for="return-date-input"
                        class="form-label"
                      >
                        Return date
                      </label>
                      <div class="input-group">
                        <span class="input-group-text">
                          <i class="bi-calendar-fill"></i>{" "}
                        </span>
                        <input
                          type="date"
                          class="form-control"
                          id="return-date-input"
                          aria-describedby="return-date-label"
                        />
                      </div>
                    </div>
                  </div>
                </div>
                {/* <!-- ... --> */}
              </div>
            </div>
          </div>
          <div class="mb-2 col">
            <div class="h-100 card">
              <div class="card-body">
                <h5 class="card-title">Details</h5>
                <div class="input-group">
                  <label for="adults-input" class="input-group-text">
                    Adults
                  </label>
                  <input
                    type="number"
                    min="0"
                    class="form-control"
                    id="adults-input"
                    aria-describedby="adults-label"
                  />
                </div>
                <span id="adults-label" class="form-text">
                  12 years old and older
                </span>
              </div>

              <div class="input-group">
                <label for="children-input" class="input-group-text">
                  Children
                </label>
                <input
                  type="number"
                  min="0"
                  class="form-control"
                  id="children-input"
                  aria-describedby="children-label"
                />
              </div>
              <span id="children-label" class="form-text">
                2 to 12 years old
              </span>
            </div>
          </div>
        </div>
      </div>
      <button id="search-button" class="w-50 btn btn-primary">
        Search
      </button>

      {/* <!-- ... --> */}
    </>
  );
};
