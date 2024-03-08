/* @odoo-module */

import { GanttRenderer } from "@web_gantt/gantt_renderer";
import { ganttView } from "@web_gantt/gantt_view";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class AvatarGanttRenderer extends GanttRenderer {
  static templete = "stock_transport.AvatarGanttRenderer";
  setup() {
    super.setup();
    this._renderVehicleNames();
  }

  async _renderVehicleNames() {
    const records = this.props.model.data.records;
    const vehicles = records.map((record) => record.vehicle_id[1]);
    this.state.vehicleNames = vehicles;
  }
}

export const saleTransportGanttView = {
  ...ganttView,
  Renderer: AvatarGanttRenderer,
};

registry
  .category("views")
  .add("stock_transport_gantt_view", saleTransportGanttView);
