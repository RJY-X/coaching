
document.addEventListener('DOMContentLoaded', () => {
    const calendar = new VanillaCalendar('#calendar',options);
    calendar.init();})

const options = {
  actions: {
    clickDay(event, self) {
      document.querySelector('html').setAttribute('selected_day',JSON.stringify(self.selectedDates))
    },
  },
  settings: {
    selection:{
      day:'multiple-ranged'    
    },


    visibility: {

      theme: 'dark',
    },
  },
  CSSClasses: {
    calendar: 'vanilla-calendar',
    calendarDefault: 'vanilla-calendar_default',
    calendarMultiple: 'vanilla-calendar_multiple',
    calendarMonth: 'vanilla-calendar_month',
    calendarYear: 'vanilla-calendar_year',
    calendarHidden: 'vanilla-calendar_hidden',
    calendarToInput: 'vanilla-calendar_to-input',
    controls: 'vanilla-calendar-controls',
    grid: 'vanilla-calendar-grid',
    gridDisabled: 'vanilla-calendar-grid_disabled',
    column: 'vanilla-calendar-column',
    columnMonth: 'vanilla-calendar-column_month',
    columnYear: 'vanilla-calendar-column_year',
    header: 'vanilla-calendar-header',
    headerContent: 'vanilla-calendar-header__content',
    month: 'vanilla-calendar-month',
    monthDisabled: 'vanilla-calendar-month_disabled',
    year: 'vanilla-calendar-year',
    yearDisabled: 'vanilla-calendar-year_disabled',
    arrow: 'vanilla-calendar-arrow',
    arrowPrev: 'vanilla-calendar-arrow_prev',
    arrowNext: 'vanilla-calendar-arrow_next',
    wrapper: 'vanilla-calendar-wrapper',
    content: 'vanilla-calendar-content',
    week: 'vanilla-calendar-week',
    weekDay: 'vanilla-calendar-week__day',
    weekDayWeekend: 'vanilla-calendar-week__day_weekend',
    days: 'vanilla-calendar-days',
    daysSelecting: 'vanilla-calendar-days_selecting',
    months: 'vanilla-calendar-months',
    monthsSelecting: 'vanilla-calendar-months_selecting',
    monthsMonth: 'vanilla-calendar-months__month',
    monthsMonthSelected: 'vanilla-calendar-months__month_selected',
    monthsMonthDisabled: 'vanilla-calendar-months__month_disabled',
    years: 'vanilla-calendar-years',
    yearsSelecting: 'vanilla-calendar-years_selecting',
    yearsYear: 'vanilla-calendar-years__year',
    yearsYearSelected: 'vanilla-calendar-years__year_selected',
    yearsYearDisabled: 'vanilla-calendar-years__year_disabled',
    time: 'vanilla-calendar-time',
    timeContent: 'vanilla-calendar-time__content',
    timeHours: 'vanilla-calendar-time__hours',
    timeMinutes: 'vanilla-calendar-time__minutes',
    timeKeeping: 'vanilla-calendar-time__keeping',
    timeRanges: 'vanilla-calendar-time__ranges',
    timeRange: 'vanilla-calendar-time__range',
    day: 'vanilla-calendar-day',
    daySelected: 'vanilla-calendar-day_selected',
    daySelectedFirst: 'vanilla-calendar-day_selected-first',
    daySelectedLast: 'vanilla-calendar-day_selected-last',
    daySelectedIntermediate: 'vanilla-calendar-day_selected-intermediate',
    dayPopup: 'vanilla-calendar-day__popup',
    dayBtn: 'vanilla-calendar-day__btn',
    dayBtnPrev: 'vanilla-calendar-day__btn_prev',
    dayBtnNext: 'vanilla-calendar-day__btn_next',
    dayBtnToday: 'vanilla-calendar-day__btn_today',
    dayBtnSelected: 'vanilla-calendar-day__btn_selected',
    dayBtnHover: 'vanilla-calendar-day__btn_hover',
    dayBtnDisabled: 'vanilla-calendar-day__btn_disabled',
    dayBtnIntermediate: 'vanilla-calendar-day__btn_intermediate',
    dayBtnWeekend: 'vanilla-calendar-day__btn_weekend',
    dayBtnHoliday: 'vanilla-calendar-day__btn_holiday',
    weekNumbers: 'vanilla-calendar-week-numbers',
    weekNumbersTitle: 'vanilla-calendar-week-numbers__title',
    weekNumbersContent: 'vanilla-calendar-week-numbers__content',
    weekNumber: 'vanilla-calendar-week-number',
    isFocus: 'vanilla-calendar-is-focus',
  },

};
