#ifndef RADIO_COUNT_TO_LEDS_H
#define RADIO_COUNT_TO_LEDS_H

/* con nx_ tinyos indica il fatto che è un tipo di dato
 * usato in un pacchetto radio */

#define SOURCE_NODE	1

#include "VarianteK.h"

typedef nx_struct radio_count_msg {
  nx_uint16_t id;
  nx_uint16_t seq;
  nx_uint16_t message;
} radio_count_msg_t;

enum {
  AM_RADIO_COUNT_MSG = 6,
};



#endif
