# encoding: utf-8

"""
Copyright (c) 2017, Ernesto Ruge
All rights reserved.
Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from flask_wtf import FlaskForm
from flask_babel import _
from wtforms import validators
from wtforms import StringField, TextAreaField, SelectField, SubmitField, HiddenField
from ..common.form import SearchBaseForm
from ..common.countrycodes import country_codes
from ..common.form_field import RegionField
from ..common.form_filter import float_filter


class StoreSearchForm(SearchBaseForm):
    name = StringField(
        label='Name'
    )
    sort_field = SelectField(
        label='Sortier-Feld',
        choices=[
            ('name', 'Name'),
            ('created', 'Erstellt')
        ]
    )


class StoreForm(FlaskForm):
    class Meta:
        locales = ('de_DE', 'de')

    name = StringField(
        label=_('Name'),
        validators=[
            validators.DataRequired(
                message=_('Bitte geben Sie einen Namen an.')
            )
        ]
    )
    type = SelectField(
        label=_('Art des Geschäfts'),
        choices=[
            ('0', 'bitte wählen'),
            ('Apotheke', 'Apotheke'),
            ('Bäckerei', 'Bäckerei'),
            ('Restaurant', 'Restaurant')
        ],
        validators=[
            validators.DataRequired(
                message='Bitte geben Sie einen Typen an.'
            ),
            validators.NoneOf(
                ['0'],
                message='Bitte geben Sie einen Typen an.'
            )
        ]
    )
    region = RegionField(
        label=_('Region'),

    )
    firstname = StringField(
        label=_('Vorname')
    )
    lastname = StringField(
        label=_('Nachname')
    )
    company = StringField(
        label=_('Unternehmen')
    )
    address = StringField(
        label=_('Straße und Hausnummer'),
        validators=[
            validators.DataRequired(
                message=_('Bitte geben Sie eine Straße und Hausnummer an.')
            )
        ]
    )
    postalcode = StringField(
        label=_('Postleitzahl'),
        validators=[
            validators.DataRequired(
                message=_('Bitte geben Sie eine Postleitzahl an.')
            )
        ]
    )
    locality = StringField(
        label=_('Ort'),
        validators=[
            validators.DataRequired(
                message=_('Bitte geben Sie einen Ort an.')
            )
        ]
    )
    country = SelectField(
        _('Staat'),
        validators=[
            validators.DataRequired(
                message=_('Bitte geben Sie einen Staat an.')
            )
        ],
        choices=country_codes,
        default='DE'
    )
    lat = HiddenField(
        label=_('Längengrad'),
        filters=[
            float_filter
        ]
    )
    lon = HiddenField(
        label=_('Breitengrad'),
        filters=[
            float_filter
        ]
    )
    website = StringField(
        label=_('Website'),
        validators=[
            validators.url(
                message='Bitte geben Sie eine URL an'
            ),
            validators.Optional()
        ],
    )
    email = StringField(
        label=_('E-Mail'),
        validators=[
            validators.email(
                message='Bitte geben Sie eine E-Mail an'
            ),
            validators.Optional()
        ],
    )
    phone = StringField(
        label=_('Telefon')
    )
    mobile = StringField(
        label=_('Mobiltelefon')
    )
    fax = StringField(
        label=_('Fax')
    )
    description = TextAreaField(
        label='Beschreibung'
    )
    submit = SubmitField(_('speichern'))


class StoreDeleteForm(FlaskForm):
    submit = SubmitField(_('löschen'))
    abort = SubmitField(_('abbrechen'))

